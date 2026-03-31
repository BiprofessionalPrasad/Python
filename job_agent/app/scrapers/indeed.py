import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from datetime import datetime, timedelta
from .base import BaseScraper, JobData
import logging
import re

logger = logging.getLogger(__name__)

class IndeedScraper(BaseScraper):
    """Scraper for Indeed job postings"""
    
    def __init__(self):
        super().__init__("Indeed")
        self.base_url = "https://www.indeed.com/jobs"
        self.country_domains = {
            'us': 'https://www.indeed.com',
            'uk': 'https://www.indeed.co.uk',
            'ca': 'https://www.indeed.ca',
            'au': 'https://www.indeed.com.au',
            'de': 'https://www.indeed.de',
            'fr': 'https://www.indeed.fr',
        }
    
    def search_jobs(self, keywords: str, location: Optional[str] = None,
                   job_type: Optional[str] = None, remote: bool = False,
                   max_results: int = 50, country: str = 'us') -> List[JobData]:
        """Search for jobs on Indeed"""
        jobs = []
        
        try:
            base_url = self.country_domains.get(country, self.country_domains['us'])
            
            # Build search parameters
            params = {
                'q': keywords,
                'l': location or '',
            }
            
            # Add remote filter
            if remote:
                params['remote'] = '1'
            
            # Add job type filter
            if job_type:
                job_type_map = {
                    'full-time': 'fulltime',
                    'part-time': 'parttime',
                    'contract': 'contract',
                    'temporary': 'temporary',
                    'internship': 'internship',
                    'commission': 'commission'
                }
                if job_type.lower() in job_type_map:
                    params['jt'] = job_type_map[job_type.lower()]
            
            start = 0
            while len(jobs) < max_results:
                params['start'] = start
                
                response = requests.get(
                    f"{base_url}/jobs",
                    params=params,
                    headers=self.headers,
                    timeout=30
                )
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find job cards
                job_cards = soup.find_all('div', {'class': 'job_seen_beacon'})
                
                if not job_cards:
                    # Try alternative selector
                    job_cards = soup.find_all('div', {'data-testid': 'job-title'})
                
                if not job_cards:
                    break
                
                for card in job_cards:
                    if len(jobs) >= max_results:
                        break
                    
                    try:
                        job = self._parse_job_card(card, base_url)
                        if job:
                            jobs.append(job)
                    except Exception as e:
                        logger.error(f"Error parsing Indeed job card: {e}")
                        continue
                
                # Move to next page (Indeed shows 15 results per page)
                start += 15
                
                # Break if no more results
                if len(job_cards) < 15:
                    break
        
        except Exception as e:
            logger.error(f"Error searching Indeed jobs: {e}")
        
        return jobs
    
    def _parse_job_card(self, card, base_url: str) -> Optional[JobData]:
        """Parse an Indeed job card"""
        try:
            # Extract job title
            title_elem = card.find('h2', {'class': 'jobTitle'})
            if not title_elem:
                title_elem = card.find('a', {'data-testid': 'job-title'})
            
            title = title_elem.text.strip() if title_elem else "Unknown"
            
            # Extract company
            company_elem = card.find('span', {'class': 'companyName'})
            if not company_elem:
                company_elem = card.find('span', {'data-testid': 'company-name'})
            
            company = company_elem.text.strip() if company_elem else "Unknown"
            
            # Extract location
            location_elem = card.find('div', {'class': 'companyLocation'})
            if not location_elem:
                location_elem = card.find('div', {'data-testid': 'job-location'})
            
            location = location_elem.text.strip() if location_elem else None
            
            # Extract job URL
            link_elem = card.find('a', {'class': 'jcs-JobTitle'})
            if not link_elem:
                link_elem = card.find('a', {'data-testid': 'job-title'})
            
            job_url = None
            job_id = None
            if link_elem:
                href = link_elem.get('href', '')
                if href.startswith('/'):
                    job_url = f"{base_url}{href}"
                else:
                    job_url = href
                
                # Extract job ID
                job_id_match = re.search(r'jk=([^&]+)', href)
                if job_id_match:
                    job_id = job_id_match.group(1)
            
            # Extract salary if available
            salary_elem = card.find('div', {'class': 'salary-snippet-container'})
            if not salary_elem:
                salary_elem = card.find('div', {'data-testid': 'job-salary'})
            
            salary = salary_elem.text.strip() if salary_elem else None
            
            # Extract job type
            job_type_elem = card.find('div', {'class': 'attribute_snippet'})
            job_type = None
            if job_type_elem:
                job_type_text = job_type_elem.text.strip().lower()
                if 'full-time' in job_type_text:
                    job_type = 'Full-time'
                elif 'part-time' in job_type_text:
                    job_type = 'Part-time'
                elif 'contract' in job_type_text:
                    job_type = 'Contract'
            
            # Check if remote
            is_remote = self.is_remote_job(title, "", location or "")
            
            # Extract posted date
            date_elem = card.find('span', {'class': 'date'})
            posted_date = None
            if date_elem:
                date_text = date_elem.text.strip()
                posted_date = self._parse_relative_date(date_text)
            
            return JobData(
                title=title,
                company=company,
                location=location,
                salary=salary,
                job_type=job_type,
                source="Indeed",
                source_url=job_url,
                external_id=job_id,
                posted_date=posted_date,
                remote=is_remote
            )
        
        except Exception as e:
            logger.error(f"Error parsing Indeed job card: {e}")
            return None
    
    def _parse_relative_date(self, date_text: str) -> Optional[datetime]:
        """Parse relative dates like '2 days ago'"""
        
        try:
            date_text = date_text.lower()
            
            # Handle "Just posted" or "Today"
            if 'just' in date_text or 'today' in date_text:
                return datetime.now()
            
            # Handle "X days ago"
            days_match = re.search(r'(\d+)\+?\s*day', date_text)
            if days_match:
                days = int(days_match.group(1))
                return datetime.now() - timedelta(days=days)
            
            # Handle "X hours ago"
            hours_match = re.search(r'(\d+)\+?\s*hour', date_text)
            if hours_match:
                hours = int(hours_match.group(1))
                return datetime.now() - timedelta(hours=hours)
            
            return None
        
        except Exception:
            return None
    
    def get_job_details(self, job_url: str) -> Optional[JobData]:
        """Get detailed job information from Indeed"""
        try:
            response = requests.get(job_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Parse job details
            title_elem = soup.find('h1', {'class': 'jobsearch-JobInfoHeader-title'})
            company_elem = soup.find('div', {'class': 'jobsearch-CompanyInfoWithoutHeaderImage'})
            if not company_elem:
                company_elem = soup.find('div', {'class': 'jobsearch-InlineCompanyRating'})
            
            description_elem = soup.find('div', {'class': 'jobsearch-jobDescriptionText'})
            
            title = title_elem.text.strip() if title_elem else "Unknown"
            company = company_elem.text.strip() if company_elem else "Unknown"
            description = description_elem.text.strip() if description_elem else None
            
            # Extract location from description or page
            location = None
            location_elem = soup.find('div', {'class': 'jobsearch-JobInfoHeader-subtitle'})
            if location_elem:
                location = location_elem.text.strip()
            
            # Determine job type and remote status
            job_type = None
            is_remote = False
            if description:
                desc_lower = description.lower()
                if 'full-time' in desc_lower or 'full time' in desc_lower:
                    job_type = 'Full-time'
                elif 'part-time' in desc_lower or 'part time' in desc_lower:
                    job_type = 'Part-time'
                elif 'contract' in desc_lower:
                    job_type = 'Contract'
                
                is_remote = self.is_remote_job(title, description, location or "")
            
            # Extract job ID from URL
            job_id_match = re.search(r'jk=([^&]+)', job_url)
            job_id = job_id_match.group(1) if job_id_match else None
            
            return JobData(
                title=title,
                company=company,
                location=location,
                description=description,
                job_type=job_type,
                source="Indeed",
                source_url=job_url,
                external_id=job_id,
                remote=is_remote
            )
        
        except Exception as e:
            logger.error(f"Error getting Indeed job details: {e}")
            return None