# Job Agent - Job Aggregator & Application Tracker

A comprehensive job search tool that aggregates listings from multiple sources (LinkedIn, Indeed, Glassdoor) and provides powerful application tracking capabilities.

## Features

### 🔍 Job Aggregation
- **Multi-source scraping**: Search jobs from LinkedIn, Indeed, and Glassdoor simultaneously
- **Deduplication**: Automatically removes duplicate listings across sources
- **Advanced filtering**: Filter by keywords, location, job type, remote work, and more
- **Real-time search**: Scrape fresh job listings on demand

### 📊 Application Tracking
- **Pipeline management**: Track applications through various stages (Applied → Screening → Interview → Offer)
- **Event timeline**: Log interviews, phone screens, assessments, and follow-ups
- **Contact management**: Store recruiter information and communication history
- **Notes & documents**: Attach notes and track which resume/cover letter was used

### 📈 Analytics & Insights
- **Dashboard overview**: Quick stats on jobs, applications, and pipeline
- **Visual pipeline**: See your application funnel at a glance
- **Success metrics**: Track response rates, interview rates, and offer rates
- **Source analysis**: Understand which job sources work best for you

### 🎨 Modern UI
- **Responsive design**: Works on desktop, tablet, and mobile
- **Clean interface**: Modern, intuitive design with smooth interactions
- **Dark navbar**: Professional appearance with gradient accents

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or download the project**:
```bash
cd job_agent
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

3. **Activate the virtual environment**:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Run the application**:
```bash
python run.py
```

6. **Open your browser** and navigate to:
```
http://localhost:5000
```

## Usage

### Dashboard
- View quick stats and recent applications
- Use the quick search to find jobs across all sources
- See your application pipeline visualization

### Jobs Page
- Browse all scraped job listings
- Filter by source, location, remote status, and more
- Save interesting jobs for later
- Mark jobs as applied
- Click on any job to see full details

### Scraping New Jobs
1. Click the "🔄" button on the Jobs page
2. Enter keywords (e.g., "Software Engineer", "Python Developer")
3. Optionally specify location and job type
4. Select which sources to search (LinkedIn, Indeed, Glassdoor)
5. Click "Start Scraping"
6. Found jobs are automatically saved to the database

### Application Tracking
1. Go to the Applications page
2. Click "Add Application"
3. Select a job from your saved listings
4. Set the application status
5. Add recruiter contact information
6. Track events (interviews, follow-ups) in the timeline

### Statistics
- View detailed analytics on your job search
- See pipeline distribution and success rates
- Track which sources are most effective

## Project Structure

```
job_agent/
├── app/
│   ├── __init__.py          # Flask app initialization & routes
│   ├── models/
│   │   └── __init__.py      # Database models (Job, Application, etc.)
│   ├── scrapers/
│   │   ├── __init__.py      # Scraper manager
│   │   ├── base.py          # Base scraper class
│   │   ├── linkedin.py      # LinkedIn scraper
│   │   ├── indeed.py        # Indeed scraper
│   │   └── glassdoor.py     # Glassdoor scraper
│   ├── templates/
│   │   ├── index.html       # Dashboard
│   │   ├── jobs.html        # Jobs listing page
│   │   ├── applications.html # Application tracker
│   │   └── stats.html       # Statistics page
│   └── static/              # Static assets (CSS, JS, images)
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md               # This file
```

## API Endpoints

### Jobs
- `GET /api/jobs` - List jobs with filtering and pagination
- `GET /api/jobs/<id>` - Get specific job details
- `PUT /api/jobs/<id>` - Update job (save/apply status)
- `DELETE /api/jobs/<id>` - Delete job
- `POST /api/jobs/<id>/notes` - Add note to job

### Search
- `POST /api/search` - Search and scrape jobs from multiple sources
- `GET /api/sources` - Get available job sources

### Applications
- `GET /api/applications` - List all applications
- `POST /api/applications` - Create new application
- `GET /api/applications/<id>` - Get application details
- `PUT /api/applications/<id>` - Update application
- `POST /api/applications/<id>/events` - Add event to application

### Statistics
- `GET /api/stats` - Get dashboard statistics
- `GET /api/stats/pipeline` - Get pipeline statistics

## Configuration

The application uses SQLite by default for simplicity. To use a different database:

1. Set the `DATABASE_URL` environment variable:
```bash
export DATABASE_URL="postgresql://user:password@localhost/jobagent"
```

2. Or modify `app/__init__.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-url'
```

## Notes

- **Web scraping**: This tool uses web scraping to gather job listings. Be respectful of the source websites' terms of service and rate limits.
- **Data persistence**: All data is stored locally in a SQLite database (`job_agent.db`).
- **Browser compatibility**: The UI works best in modern browsers (Chrome, Firefox, Safari, Edge).

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure you've activated the virtual environment and installed all requirements.

2. **Database errors**: Delete `job_agent.db` and restart the application to recreate the database.

3. **Scraping failures**: Some websites may block scrapers. The tool includes headers to mimic a real browser, but results may vary.

4. **Port already in use**: Change the port in `run.py`:
```python
app.run(host='0.0.0.0', port=5001)  # Use a different port
```

## Future Enhancements

- [ ] Email notifications for application follow-ups
- [ ] Resume/CV builder and storage
- [ ] Cover letter templates
- [ ] Interview preparation resources
- [ ] Salary insights and comparisons
- [ ] Job alerts and scheduled scraping
- [ ] Export data to Excel/CSV
- [ ] Mobile app

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

**Happy job hunting! 🚀**