from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255))
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    salary = db.Column(db.String(100))
    job_type = db.Column(db.String(50))  # Full-time, Part-time, Contract, etc.
    remote = db.Column(db.Boolean, default=False)
    
    # Source information
    source = db.Column(db.String(50), nullable=False)  # LinkedIn, Indeed, etc.
    source_url = db.Column(db.Text)
    external_id = db.Column(db.String(255))  # ID from the source
    
    # Metadata
    posted_date = db.Column(db.DateTime)
    scraped_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Status
    is_active = db.Column(db.Boolean, default=True)
    is_saved = db.Column(db.Boolean, default=False)
    is_applied = db.Column(db.Boolean, default=False)
    
    # Relationships
    applications = db.relationship('Application', backref='job', lazy=True, cascade='all, delete-orphan')
    notes = db.relationship('JobNote', backref='job', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'requirements': self.requirements,
            'salary': self.salary,
            'job_type': self.job_type,
            'remote': self.remote,
            'source': self.source,
            'source_url': self.source_url,
            'external_id': self.external_id,
            'posted_date': self.posted_date.isoformat() if self.posted_date else None,
            'scraped_date': self.scraped_date.isoformat() if self.scraped_date else None,
            'is_active': self.is_active,
            'is_saved': self.is_saved,
            'is_applied': self.is_applied
        }

class Application(db.Model):
    __tablename__ = 'applications'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    
    # Application details
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='applied')  # applied, screening, interview, offer, rejected, withdrawn
    
    # Contact information
    recruiter_name = db.Column(db.String(255))
    recruiter_email = db.Column(db.String(255))
    recruiter_phone = db.Column(db.String(50))
    
    # Application materials
    resume_used = db.Column(db.String(255))
    cover_letter_used = db.Column(db.String(255))
    
    # Follow-up
    follow_up_date = db.Column(db.DateTime)
    last_contact_date = db.Column(db.DateTime)
    
    # Notes
    notes = db.Column(db.Text)
    
    # Timeline of events
    events = db.relationship('ApplicationEvent', backref='application', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'job': self.job.to_dict() if self.job else None,
            'applied_date': self.applied_date.isoformat() if self.applied_date else None,
            'status': self.status,
            'recruiter_name': self.recruiter_name,
            'recruiter_email': self.recruiter_email,
            'recruiter_phone': self.recruiter_phone,
            'resume_used': self.resume_used,
            'cover_letter_used': self.cover_letter_used,
            'follow_up_date': self.follow_up_date.isoformat() if self.follow_up_date else None,
            'last_contact_date': self.last_contact_date.isoformat() if self.last_contact_date else None,
            'notes': self.notes,
            'events': [event.to_dict() for event in self.events]
        }

class ApplicationEvent(db.Model):
    __tablename__ = 'application_events'
    
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=False)
    
    event_type = db.Column(db.String(50), nullable=False)  # interview, phone_screen, assessment, etc.
    event_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(255))  # For in-person or video link
    result = db.Column(db.String(50))  # pending, passed, failed, etc.
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'application_id': self.application_id,
            'event_type': self.event_type,
            'event_date': self.event_date.isoformat() if self.event_date else None,
            'description': self.description,
            'location': self.location,
            'result': self.result,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class JobNote(db.Model):
    __tablename__ = 'job_notes'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'content': self.content,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class SearchFilter(db.Model):
    __tablename__ = 'search_filters'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.String(500))
    location = db.Column(db.String(255))
    job_type = db.Column(db.String(50))
    remote_only = db.Column(db.Boolean, default=False)
    min_salary = db.Column(db.Integer)
    max_salary = db.Column(db.Integer)
    sources = db.Column(db.String(500))  # JSON array of sources
    
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_run = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'keywords': self.keywords,
            'location': self.location,
            'job_type': self.job_type,
            'remote_only': self.remote_only,
            'min_salary': self.min_salary,
            'max_salary': self.max_salary,
            'sources': json.loads(self.sources) if self.sources else [],
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_run': self.last_run.isoformat() if self.last_run else None
        }

class StatsSummary(db.Model):
    __tablename__ = 'stats_summary'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow().date, unique=True)
    
    # Job stats
    total_jobs = db.Column(db.Integer, default=0)
    new_jobs_today = db.Column(db.Integer, default=0)
    
    # Application stats
    total_applications = db.Column(db.Integer, default=0)
    applications_today = db.Column(db.Integer, default=0)
    
    # Status breakdown
    status_applied = db.Column(db.Integer, default=0)
    status_screening = db.Column(db.Integer, default=0)
    status_interview = db.Column(db.Integer, default=0)
    status_offer = db.Column(db.Integer, default=0)
    status_rejected = db.Column(db.Integer, default=0)
    status_withdrawn = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat() if self.date else None,
            'total_jobs': self.total_jobs,
            'new_jobs_today': self.new_jobs_today,
            'total_applications': self.total_applications,
            'applications_today': self.applications_today,
            'status_breakdown': {
                'applied': self.status_applied,
                'screening': self.status_screening,
                'interview': self.status_interview,
                'offer': self.status_offer,
                'rejected': self.status_rejected,
                'withdrawn': self.status_withdrawn
            }
        }