from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 
    'sqlite:///job_agent.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS
CORS(app)

# Initialize database
from app.models import db, Job, Application, ApplicationEvent, JobNote, SearchFilter, StatsSummary
db.init_app(app)

# Import scrapers
from app.scrapers import ScraperManager
scraper_manager = ScraperManager()

# Create tables
with app.app_context():
    db.create_all()

# ==================== HTML ROUTES ====================

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/jobs')
def jobs_page():
    """Jobs listing page"""
    return render_template('jobs.html')

@app.route('/applications')
def applications_page():
    """Applications tracking page"""
    return render_template('applications.html')

@app.route('/stats')
def stats_page():
    """Statistics page"""
    return render_template('stats.html')

# ==================== API ROUTES - JOBS ====================

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """Get jobs with filtering and pagination"""
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        search = request.args.get('search', '')
        source = request.args.get('source', '')
        location = request.args.get('location', '')
        remote = request.args.get('remote', type=bool)
        saved = request.args.get('saved', type=bool)
        applied = request.args.get('applied', type=bool)
        
        # Build query
        query = Job.query
        
        if search:
            search_filter = f'%{search}%'
            query = query.filter(
                db.or_(
                    Job.title.ilike(search_filter),
                    Job.company.ilike(search_filter),
                    Job.description.ilike(search_filter)
                )
            )
        
        if source:
            query = query.filter(Job.source == source)
        
        if location:
            query = query.filter(Job.location.ilike(f'%{location}%'))
        
        if remote is not None:
            query = query.filter(Job.remote == remote)
        
        if saved is not None:
            query = query.filter(Job.is_saved == saved)
        
        if applied is not None:
            query = query.filter(Job.is_applied == applied)
        
        # Order by scraped date (newest first)
        query = query.order_by(Job.scraped_date.desc())
        
        # Paginate
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        
        return jsonify({
            'success': True,
            'jobs': [job.to_dict() for job in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        })
    
    except Exception as e:
        logger.error(f"Error getting jobs: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Get a specific job by ID"""
    try:
        job = Job.query.get_or_404(job_id)
        return jsonify({'success': True, 'job': job.to_dict()})
    except Exception as e:
        logger.error(f"Error getting job {job_id}: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    """Update a job"""
    try:
        job = Job.query.get_or_404(job_id)
        data = request.get_json()
        
        if 'is_saved' in data:
            job.is_saved = data['is_saved']
        
        if 'is_applied' in data:
            job.is_applied = data['is_applied']
        
        if 'is_active' in data:
            job.is_active = data['is_active']
        
        db.session.commit()
        
        return jsonify({'success': True, 'job': job.to_dict()})
    except Exception as e:
        logger.error(f"Error updating job {job_id}: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """Delete a job"""
    try:
        job = Job.query.get_or_404(job_id)
        db.session.delete(job)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Job deleted successfully'})
    except Exception as e:
        logger.error(f"Error deleting job {job_id}: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/jobs/<int:job_id>/notes', methods=['POST'])
def add_job_note(job_id):
    """Add a note to a job"""
    try:
        job = Job.query.get_or_404(job_id)
        data = request.get_json()
        
        note = JobNote(
            job_id=job_id,
            content=data.get('content', '')
        )
        
        db.session.add(note)
        db.session.commit()
        
        return jsonify({'success': True, 'note': note.to_dict()})
    except Exception as e:
        logger.error(f"Error adding note to job {job_id}: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== API ROUTES - SEARCH ====================

@app.route('/api/search', methods=['POST'])
def search_jobs():
    """Search for jobs across multiple sources"""
    try:
        data = request.get_json()
        
        keywords = data.get('keywords', '')
        location = data.get('location', '')
        job_type = data.get('job_type', '')
        remote = data.get('remote', False)
        sources = data.get('sources', None)
        max_results = data.get('max_results', 25)
        
        if not keywords:
            return jsonify({'success': False, 'error': 'Keywords are required'}), 400
        
        # Run scrapers
        results = scraper_manager.search_all(
            keywords=keywords,
            location=location,
            job_type=job_type,
            remote=remote,
            max_results_per_source=max_results,
            sources=sources
        )
        
        # Flatten and deduplicate results
        all_jobs = scraper_manager.get_all_jobs(results)
        unique_jobs = scraper_manager.deduplicate_jobs(all_jobs)
        
        # Save jobs to database
        saved_count = 0
        for job_data in unique_jobs:
            # Check if job already exists
            existing = Job.query.filter_by(
                external_id=job_data.external_id,
                source=job_data.source
            ).first()
            
            if not existing:
                job = Job(
                    title=job_data.title,
                    company=job_data.company,
                    location=job_data.location,
                    description=job_data.description,
                    requirements=job_data.requirements,
                    salary=job_data.salary,
                    job_type=job_data.job_type,
                    remote=job_data.remote,
                    source=job_data.source,
                    source_url=job_data.source_url,
                    external_id=job_data.external_id,
                    posted_date=job_data.posted_date
                )
                db.session.add(job)
                saved_count += 1
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'jobs_found': len(unique_jobs),
            'jobs_saved': saved_count,
            'sources': {k: len(v) for k, v in results.items()}
        })
    
    except Exception as e:
        logger.error(f"Error searching jobs: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/sources', methods=['GET'])
def get_sources():
    """Get available job sources"""
    return jsonify({
        'success': True,
        'sources': scraper_manager.get_available_sources()
    })

# ==================== API ROUTES - APPLICATIONS ====================

@app.route('/api/applications', methods=['GET'])
def get_applications():
    """Get all job applications"""
    try:
        status = request.args.get('status', '')
        
        query = Application.query.join(Job)
        
        if status:
            query = query.filter(Application.status == status)
        
        query = query.order_by(Application.applied_date.desc())
        
        applications = query.all()
        
        return jsonify({
            'success': True,
            'applications': [app.to_dict() for app in applications]
        })
    except Exception as e:
        logger.error(f"Error getting applications: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/applications', methods=['POST'])
def create_application():
    """Create a new job application"""
    try:
        data = request.get_json()
        
        job_id = data.get('job_id')
        if not job_id:
            return jsonify({'success': False, 'error': 'Job ID is required'}), 400
        
        job = Job.query.get_or_404(job_id)
        
        # Create application
        application = Application(
            job_id=job_id,
            status=data.get('status', 'applied'),
            recruiter_name=data.get('recruiter_name'),
            recruiter_email=data.get('recruiter_email'),
            recruiter_phone=data.get('recruiter_phone'),
            resume_used=data.get('resume_used'),
            cover_letter_used=data.get('cover_letter_used'),
            notes=data.get('notes')
        )
        
        # Update job status
        job.is_applied = True
        
        db.session.add(application)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'application': application.to_dict()
        })
    
    except Exception as e:
        logger.error(f"Error creating application: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/applications/<int:app_id>', methods=['GET'])
def get_application(app_id):
    """Get a specific application"""
    try:
        application = Application.query.get_or_404(app_id)
        return jsonify({'success': True, 'application': application.to_dict()})
    except Exception as e:
        logger.error(f"Error getting application {app_id}: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/applications/<int:app_id>', methods=['PUT'])
def update_application(app_id):
    """Update an application"""
    try:
        application = Application.query.get_or_404(app_id)
        data = request.get_json()
        
        if 'status' in data:
            application.status = data['status']
        
        if 'recruiter_name' in data:
            application.recruiter_name = data['recruiter_name']
        
        if 'recruiter_email' in data:
            application.recruiter_email = data['recruiter_email']
        
        if 'recruiter_phone' in data:
            application.recruiter_phone = data['recruiter_phone']
        
        if 'resume_used' in data:
            application.resume_used = data['resume_used']
        
        if 'cover_letter_used' in data:
            application.cover_letter_used = data['cover_letter_used']
        
        if 'notes' in data:
            application.notes = data['notes']
        
        if 'follow_up_date' in data:
            application.follow_up_date = datetime.fromisoformat(data['follow_up_date'])
        
        if 'last_contact_date' in data:
            application.last_contact_date = datetime.fromisoformat(data['last_contact_date'])
        
        db.session.commit()
        
        return jsonify({'success': True, 'application': application.to_dict()})
    except Exception as e:
        logger.error(f"Error updating application {app_id}: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/applications/<int:app_id>/events', methods=['POST'])
def add_application_event(app_id):
    """Add an event to an application"""
    try:
        application = Application.query.get_or_404(app_id)
        data = request.get_json()
        
        event = ApplicationEvent(
            application_id=app_id,
            event_type=data.get('event_type', ''),
            event_date=datetime.fromisoformat(data.get('event_date')),
            description=data.get('description'),
            location=data.get('location'),
            result=data.get('result', 'pending')
        )
        
        db.session.add(event)
        db.session.commit()
        
        return jsonify({'success': True, 'event': event.to_dict()})
    except Exception as e:
        logger.error(f"Error adding event to application {app_id}: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== API ROUTES - STATS ====================

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get dashboard statistics"""
    try:
        # Total jobs
        total_jobs = Job.query.count()
        new_jobs_today = Job.query.filter(
            Job.scraped_date >= datetime.utcnow().date()
        ).count()
        
        # Saved jobs
        saved_jobs = Job.query.filter_by(is_saved=True).count()
        
        # Applications
        total_applications = Application.query.count()
        
        # Status breakdown
        status_counts = db.session.query(
            Application.status,
            db.func.count(Application.id)
        ).group_by(Application.status).all()
        
        status_breakdown = {status: count for status, count in status_counts}
        
        # Recent applications
        recent_applications = Application.query.order_by(
            Application.applied_date.desc()
        ).limit(5).all()
        
        return jsonify({
            'success': True,
            'stats': {
                'total_jobs': total_jobs,
                'new_jobs_today': new_jobs_today,
                'saved_jobs': saved_jobs,
                'total_applications': total_applications,
                'status_breakdown': status_breakdown,
                'recent_applications': [app.to_dict() for app in recent_applications]
            }
        })
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/stats/pipeline', methods=['GET'])
def get_pipeline_stats():
    """Get application pipeline statistics"""
    try:
        # Get counts for each status
        pipeline = db.session.query(
            Application.status,
            db.func.count(Application.id)
        ).group_by(Application.status).all()
        
        # Calculate conversion rates
        total = sum(count for _, count in pipeline)
        
        pipeline_data = []
        for status, count in pipeline:
            percentage = (count / total * 100) if total > 0 else 0
            pipeline_data.append({
                'status': status,
                'count': count,
                'percentage': round(percentage, 2)
            })
        
        return jsonify({
            'success': True,
            'pipeline': pipeline_data,
            'total': total
        })
    except Exception as e:
        logger.error(f"Error getting pipeline stats: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)