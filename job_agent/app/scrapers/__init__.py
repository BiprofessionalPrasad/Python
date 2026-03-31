from .linkedin import LinkedInScraper
from .indeed import IndeedScraper
from .glassdoor import GlassdoorScraper
from .base import JobData
from typing import List, Optional, Dict
import logging
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, as_completed

logger = logging.getLogger(__name__)

class ScraperManager:
    """Manager for running multiple job scrapers"""
    
    def __init__(self):
        self.scrapers = {
            'linkedin': LinkedInScraper(),
            'indeed': IndeedScraper(),
            'glassdoor': GlassdoorScraper(),
        }
    
    def search_all(self, keywords: str, location: Optional[str] = None,
                   job_type: Optional[str] = None, remote: bool = False,
                   max_results_per_source: int = 25,
                   sources: Optional[List[str]] = None) -> Dict[str, List[JobData]]:
        """
        Search for jobs across all enabled sources
        
        Args:
            keywords: Job title or keywords to search for
            location: Location filter
            job_type: Type of job
            remote: Whether to filter for remote jobs only
            max_results_per_source: Maximum results per source
            sources: List of sources to search (None = all)
            
        Returns:
            Dictionary mapping source name to list of JobData
        """
        results = {}
        
        # Determine which sources to use
        sources_to_use = sources if sources else list(self.scrapers.keys())
        
        # Use ThreadPoolExecutor for parallel scraping
        with ThreadPoolExecutor(max_workers=len(sources_to_use)) as executor:
            future_to_source = {}
            
            for source_name in sources_to_use:
                if source_name in self.scrapers:
                    scraper = self.scrapers[source_name]
                    future = executor.submit(
                        scraper.search_jobs,
                        keywords=keywords,
                        location=location,
                        job_type=job_type,
                        remote=remote,
                        max_results=max_results_per_source
                    )
                    future_to_source[future] = source_name
            
            # Collect results as they complete
            for future in as_completed(future_to_source):
                source_name = future_to_source[future]
                try:
                    jobs = future.result()
                    results[source_name] = jobs
                    logger.info(f"Found {len(jobs)} jobs from {source_name}")
                except Exception as e:
                    logger.error(f"Error scraping {source_name}: {e}")
                    results[source_name] = []
        
        return results
    
    def get_job_details(self, source: str, job_url: str) -> Optional[JobData]:
        """Get detailed job information from a specific source"""
        if source.lower() in self.scrapers:
            return self.scrapers[source.lower()].get_job_details(job_url)
        return None
    
    def get_all_jobs(self, results: Dict[str, List[JobData]]) -> List[JobData]:
        """Flatten results from all sources into a single list"""
        all_jobs = []
        for source_jobs in results.values():
            all_jobs.extend(source_jobs)
        return all_jobs
    
    def deduplicate_jobs(self, jobs: List[JobData]) -> List[JobData]:
        """Remove duplicate jobs based on title, company, and location"""
        seen = set()
        unique_jobs = []
        
        for job in jobs:
            # Create a key for deduplication
            key = (
                self._normalize_text(job.title),
                self._normalize_text(job.company),
                self._normalize_text(job.location) if job.location else ""
            )
            
            if key not in seen:
                seen.add(key)
                unique_jobs.append(job)
        
        return unique_jobs
    
    def _normalize_text(self, text: str) -> str:
        """Normalize text for comparison"""
        return ' '.join(text.lower().split())
    
    def get_available_sources(self) -> List[str]:
        """Get list of available scraper sources"""
        return list(self.scrapers.keys())