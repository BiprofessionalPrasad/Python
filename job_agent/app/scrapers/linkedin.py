import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from .base import BaseScraper, JobData
from datetime import datetime, timedelta
import logging
import re
import json

logger = logging.getLogger(__name__)

class LinkedInScraper(BaseScraper):
    """Scraper for LinkedIn job postings"""
    
    def __init__(self):
        super().__init__("LinkedIn")
        self.base_url = "https://www.linkedin.com/jobs/search"
        self.api_base = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/"
    
    def search_jobs(self, keywords: str, location: Optional[str] = None,
                   job_type: Optional[str] = None, remote: bool = False,
                   max_results: int = 50) -> List[JobData]:
        """Search for jobs on LinkedIn"""
        jobs = []
        
        try:
            # Build search URL
            params = {
                'keywords': keywords,
                'location': location or '',
                'f_TPR': '',  # Time posted (empty = all time)
                'start': 0
            }
            
            # Add remote filter
            if remote:
                params['f_WT'] = '2'  # Remote work type
            
            # Add job type filter
            if job_type:
                job_type_map = {
                    'full-time': 'F',
                    'part-time': 'P',
                    'contract': 'C',
                    'temporary': 'T',
                    'internship': 'I'
                }
                if job_type.lower() in job_type_map:
                    params['f_JT'] = job_type_map[job_type.lower()]
            
            headers = {
                **self.headers,
                'Referer': 'https://www.linkedin.com/jobs',
            }
            
            # Fetch multiple pages
            while len(jobs) < max_results:
                response = requests.get(
                    self.base_url,
                    params=params,
                    headers=headers,
                    timeout=30
                )
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find job listings
                job_cards = soup.find_all('div', {'class': 'base-card'})
                
                if not job_cards:
                    break
                
                for card in job_cards:
                    if len(jobs) >= max_results:
                        break
                    
                    try:
                        job = self._parse_job_card(card)
                        if job:
                            jobs.append(job)
                    except Exception as e:
                        logger.error(f"Error parsing job card: {e}")
                        continue
                
                # Move to next page
                params['start'] += 25
                
                # Break if no more results
                if len(job_cards) < 25:
                    break
        
        except Exception as e:
            logger.error(f"Error searching LinkedIn jobs: {e}")
        
        return jobs
    
    def _parse_job_card(self, card) -> Optional[JobData]:
        """Parse a LinkedIn job card"""
        try:
            # Extract job ID from URL
            link_elem = card.find('a', {'class': 'base-card__full-link'})
            if not link_elem:
                return None
            
            job_url = link_elem.get('href', '')
            job_id_match = re.search(r'/view/([^/?]+)', job_url)
            job_id = job_id_match.group(1) if job_id_match else None
            
            # Extract basic info
            title_elem = card.find('h3', {'class': 'base-search-card__title'})
            company_elem = card.find('h4', {'class': 'base-search-card__subtitle'})
            location_elem = card.find('span', {'class': 'job-search-card__location'})
            
            title = title_elem.text.strip() if title_elem else "Unknown"
            company = company_elem.text.strip() if company_elem else "Unknown"
            location = location_elem.text.strip() if location_elem else None
            
            # Check if remote
            is_remote = self.is_remote_job(title, "", location or "")
            
            # Get posted date
            time_elem = card.find('time')
            posted_date = None
            if time_elem:
                datetime_str = time_elem.get('datetime')
                posted_date = self.parse_date(datetime_str)
            
            return JobData(
                title=title,
                company=company,
                location=location,
                source="LinkedIn",
                source_url=job_url,
                external_id=job_id,
                posted_date=posted_date,
                remote=is_remote
            )
        
        except Exception as e:
            logger.error(f"Error parsing job card: {e}")
            return None
    
    def get_job_details(self, job_url: str) -> Optional[JobData]:
        """Get detailed job information from LinkedIn"""
        try:
            # Extract job ID
            job_id_match = re.search(r'/view/([^/?]+)', job_url)
            if not job_id_match:
                return None
            
            job_id = job_id_match.group(1)
            
            # Use LinkedIn's guest API
            api_url = f"{self.api_base}{job_id}"
            
            response = requests.get(api_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Parse job details
            title_elem = soup.find('h2', {'class': 'top-card-layout__title'})
            company_elem = soup.find('a', {'class': 'topcard__org-name-link'})
            location_elem = soup.find('span', {'class': 'topcard__flavor--bullet'})
            description_elem = soup.find('div', {'class': 'description__text'})
            
            # Extract salary if available
            salary_elem = soup.find('div', {'class': 'salary'})
            salary = salary_elem.text.strip() if salary_elem else None
            
            title = title_elem.text.strip() if title_elem else "Unknown"
            company = company_elem.text.strip() if company_elem else "Unknown"
            location = location_elem.text.strip() if location_elem else None
            description = description_elem.text.strip() if description_elem else None
            
            # Determine job type from description
            job_type = None
            if description:
                desc_lower = description.lower()
                if 'full-time' in desc_lower or 'full time' in desc_lower:
                    job_type = 'Full-time'
                elif 'part-time' in desc_lower or 'part time' in desc_lower:
                    job_type = 'Part-time'
                elif 'contract' in desc_lower:
                    job_type = 'Contract'
                elif 'internship' in desc_lower:
                    job_type = 'Internship'
            
            is_remote = self.is_remote_job(title, description or "", location or "")
            
            return JobData(
                title=title,
                company=company,
                location=location,
                description=description,
                salary=salary,
                job_type=job_type,
                source="LinkedIn",
                source_url=job_url,
                external_id=job_id,
                remote=is_remote
            )
        
        except Exception as e:
            logger.error(f"Error getting job details: {e}")
            return None