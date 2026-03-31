import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from .base import BaseScraper, JobData
import logging
import re

logger = logging.getLogger(__name__)

class GlassdoorScraper(BaseScraper):
    """Scraper for Glassdoor job postings"""
    
    def __init__(self):
        super().__init__("Glassdoor")
        self.base_url = "https://www.glassdoor.com/Job/jobs.htm"
    
    def search_jobs(self, keywords: str, location: Optional[str] = None,
                   job_type: Optional[str] = None, remote: bool = False,
                   max_results: int = 50) -> List[JobData]:
        """Search for jobs on Glassdoor"""
        jobs = []
        
        try:
            # Build search parameters
            params = {
                'suggestCount': '0',
                'suggestChosen': 'false',
                'clickSource': 'searchBtn',
                'typedKeyword': keywords,
                'sc.keyword': keywords,
                'locT': '',
                'locId': '',
                'jobType': '',
            }
            
            if location:
                params['sc.location'] = location
            
            # Add job type filter
            if job_type:
                job_type_map = {
                    'full-time': 'fulltime',
                    'part-time': 'parttime',
                    'contract': 'contract',
                    'internship': 'internship'
                }
                if job_type.lower() in job_type_map:
                    params['jobType'] = job_type_map[job_type.lower()]
            
            page = 1
            while len(jobs) < max_results:
                params['page'] = page
                
                response = requests.get(
                    self.base_url,
                    params=params,
                    headers=self.headers,
                    timeout=30
                )
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find job listings
                job_cards = soup.find_all('li', {'class': 'react-job-listing'})
                
                if not job_cards:
                    # Try alternative selectors
                    job_cards = soup.find_all('div', {'class': 'jobContainer'})
                
                if not job_cards:
                    break
                
                for card in job_cards:
                    if len(jobs) >= max_results:
                        break
                    
                    try:
                        job = self._parse_job_card(card)
                        if job:
                            # Filter for remote if requested
                            if remote and not job.remote:
                                continue
                            jobs.append(job)
                    except Exception as e:
                        logger.error(f"Error parsing Glassdoor job card: {e}")
                        continue
                
                page += 1
                
                # Break if no more results
                if len(job_cards) < 30:
                    break
        
        except Exception as e:
            logger.error(f"Error searching Glassdoor jobs: {e}")
        
        return jobs
    
    def _parse_job_card(self, card) -> Optional[JobData]:
        """Parse a Glassdoor job card"""
        try:
            # Extract job title
            title_elem = card.find('a', {'class': 'jobLink'})
            if not title_elem:
                title_elem = card.find('a', {'data-test': 'job-link'})
            
            title = title_elem.text.strip() if title_elem else "Unknown"
            
            # Extract company
            company_elem = card.find('a', {'class': 'job-search-key-l2wjgv'})
            if not company_elem:
                company_elem = card.find('div', {'class': 'job-search-key-1mn3dn8'})
            
            company = company_elem.text.strip() if company_elem else "Unknown"
            
            # Extract location
            location_elem = card.find('span', {'class': 'job-search-key-1c2b3t4'})
            if not location_elem:
                location_elem = card.find('span', {'data-test': 'job-location'})
            
            location = location_elem.text.strip() if location_elem else None
            
            # Extract job URL
            job_url = None
            job_id = None
            if title_elem:
                href = title_elem.get('href', '')
                if href.startswith('/'):
                    job_url = f"https://www.glassdoor.com{href}"
                else:
                    job_url = href
                
                # Extract job ID
                job_id_match = re.search(r'jobListingId=([^&]+)', href)
                if job_id_match:
                    job_id = job_id_match.group(1)
            
            # Extract salary if available
            salary_elem = card.find('span', {'class': 'job-search-key-salary'})
            salary = salary_elem.text.strip() if salary_elem else None
            
            # Check if remote
            is_remote = self.is_remote_job(title, "", location or "")
            
            # Extract posted date
            date_elem = card.find('div', {'class': 'job-search-key-days'})
            posted_date = None
            if date_elem:
                date_text = date_elem.text.strip()
                posted_date = self._parse_relative_date(date_text)
            
            return JobData(
                title=title,
                company=company,
                location=location,
                salary=salary,
                source="Glassdoor",
                source_url=job_url,
                external_id=job_id,
                posted_date=posted_date,
                remote=is_remote
            )
        
        except Exception as e:
            logger.error(f"Error parsing Glassdoor job card: {e}")
            return None
    
    def _parse_relative_date(self, date_text: str) -> Optional[datetime]:
        """Parse relative dates like '2d' or '1w'"""
        from datetime import datetime, timedelta
        import re
        
        try:
            date_text = date_text.lower()
            
            # Handle days
            days_match = re.search(r'(\d+)\s*d', date_text)
            if days_match:
                days = int(days_match.group(1))
                return datetime.now() - timedelta(days=days)
            
            # Handle weeks
            weeks_match = re.search(r'(\d+)\s*w', date_text)
            if weeks_match:
                weeks = int(weeks_match.group(1))
                return datetime.now() - timedelta(weeks=weeks)
            
            # Handle hours
            hours_match = re.search(r'(\d+)\s*h', date_text)
            if hours_match:
                hours = int(hours_match.group(1))
                return datetime.now() - timedelta(hours=hours)
            
            return None
        
        except Exception:
            return None
    
    def get_job_details(self, job_url: str) -> Optional[JobData]:
        """Get detailed job information from Glassdoor"""
        try:
            response = requests.get(job_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Parse job details
            title_elem = soup.find('h1', {'class': 'job-title'})
            if not title_elem:
                title_elem = soup.find('h1', {'data-test': 'job-title'})
            
            company_elem = soup.find('span', {'class': 'employer-name'})
            if not company_elem:
                company_elem = soup.find('div', {'data-test': 'employer-name'})
            
            description_elem = soup.find('div', {'class': 'jobDescriptionContent'})
            if not description_elem:
                description_elem = soup.find('div', {'data-test': 'job-description'})
            
            title = title_elem.text.strip() if title_elem else "Unknown"
            company = company_elem.text.strip() if company_elem else "Unknown"
            description = description_elem.text.strip() if description_elem else None
            
            # Extract location
            location_elem = soup.find('span', {'class': 'location'})
            if not location_elem:
                location_elem = soup.find('div', {'data-test': 'location'})
            
            location = location_elem.text.strip() if location_elem else None
            
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
            
            # Extract salary
            salary_elem = soup.find('span', {'class': 'salary'})
            salary = salary_elem.text.strip() if salary_elem else None
            
            # Extract job ID from URL
            job_id_match = re.search(r'jobListingId=([^&]+)', job_url)
            job_id = job_id_match.group(1) if job_id_match else None
            
            return JobData(
                title=title,
                company=company,
                location=location,
                description=description,
                salary=salary,
                job_type=job_type,
                source="Glassdoor",
                source_url=job_url,
                external_id=job_id,
                remote=is_remote
            )
        
        except Exception as e:
            logger.error(f"Error getting Glassdoor job details: {e}")
            return None