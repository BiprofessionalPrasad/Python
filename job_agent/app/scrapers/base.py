from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class JobData:
    """Data class for job information"""
    title: str
    company: str
    location: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = None
    remote: bool = False
    source: str = ""
    source_url: Optional[str] = None
    external_id: Optional[str] = None
    posted_date: Optional[datetime] = None
    
    def to_dict(self) -> Dict:
        return {
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
            'posted_date': self.posted_date.isoformat() if self.posted_date else None
        }

class BaseScraper(ABC):
    """Base class for all job scrapers"""
    
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.session = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
    
    @abstractmethod
    def search_jobs(self, keywords: str, location: Optional[str] = None, 
                   job_type: Optional[str] = None, remote: bool = False,
                   max_results: int = 50) -> List[JobData]:
        """
        Search for jobs on this platform
        
        Args:
            keywords: Job title or keywords to search for
            location: Location filter (optional)
            job_type: Type of job (full-time, part-time, contract, etc.)
            remote: Whether to filter for remote jobs only
            max_results: Maximum number of results to return
            
        Returns:
            List of JobData objects
        """
        pass
    
    @abstractmethod
    def get_job_details(self, job_url: str) -> Optional[JobData]:
        """
        Get detailed information about a specific job
        
        Args:
            job_url: URL of the job posting
            
        Returns:
            JobData object with full details, or None if failed
        """
        pass
    
    def clean_text(self, text: Optional[str]) -> Optional[str]:
        """Clean and normalize text content"""
        if not text:
            return None
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text.strip()
    
    def parse_date(self, date_string: str) -> Optional[datetime]:
        """Parse various date formats into datetime object"""
        if not date_string:
            return None
            
        date_formats = [
            '%Y-%m-%d',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%SZ',
            '%m/%d/%Y',
            '%d/%m/%Y',
            '%B %d, %Y',
            '%b %d, %Y',
            '%d %B %Y',
            '%d %b %Y',
            '%Y-%m-%d %H:%M:%S',
        ]
        
        for fmt in date_formats:
            try:
                return datetime.strptime(date_string, fmt)
            except ValueError:
                continue
        
        return None
    
    def is_remote_job(self, title: str, description: str, location: str) -> bool:
        """Determine if a job is remote based on various indicators"""
        remote_keywords = ['remote', 'work from home', 'wfh', 'telecommute', 
                          'virtual', 'home-based', 'anywhere', 'distributed team']
        
        text_to_check = f"{title} {description} {location}".lower()
        
        return any(keyword in text_to_check for keyword in remote_keywords)