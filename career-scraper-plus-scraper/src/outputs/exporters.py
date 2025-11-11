thonimport json

def export_data(job_data):
    # Export job data to JSON file
    with open('sample_output.json', 'w') as outfile:
        json.dump(job_data, outfile, indent=4)
    print("Job data exported to sample_output.json")