#!/usr/bin/env python3
"""
Job Agent - Job Aggregator and Application Tracker

A comprehensive job search tool that aggregates listings from multiple sources
(LikedIn, Indeed, Glassdoor) and provides application tracking capabilities.
"""

import os
import sys

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

def main():
    """Run the Flask application"""
    print("=" * 60)
    print("Job Agent - Job Aggregator & Application Tracker")
    print("=" * 60)
    print("\nStarting server...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )

if __name__ == '__main__':
    main()