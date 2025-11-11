thondef normalize_job_data(job_data):
    # Normalizing job data to a common structure
    normalized_data = []
    for job in job_data:
        normalized_data.append({
            "title": job.get("title"),
            "location": job.get("location"),
            "url": job.get("url"),
        })
    return normalized_data