thonimport json
import time
from extractors.job_parser import parse_job
from outputs.exporters import export_data
from config.settings import get_settings

def run_scraper():
    settings = get_settings()
    job_data = []
    
    # Simulate fetching job data
    for provider in settings['providers']:
        print(f"Fetching jobs from {provider}...")
        time.sleep(2)  # Simulate delay for scraping
        
        # Parsing job data for the provider
        job_data.append(parse_job(provider))

    # Export the data to output
    export_data(job_data)

if __name__ == "__main__":
    run_scraper()