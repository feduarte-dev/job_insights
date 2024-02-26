from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file) -> List[Dict]:
        with open(file) as jobs_file:
            self.jobs_list = [dict(row) for row in csv.DictReader(jobs_file)]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_jobs = set(row["job_type"] for row in self.jobs_list)
        return list(unique_jobs)

    def filter_by_multiple_criteria(self, jobs, filters) -> List[dict]:
        if not isinstance(filters, dict):
            raise TypeError("Filters must be a dictionary")

        filtered_jobs = [
            row
            for row in jobs
            if all(row.get(key) == value for key, value in filters.items())
        ]
        return filtered_jobs
