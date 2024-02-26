from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file) -> List[Dict]:
        with open(file) as jobs_file:
            jobs_reader = csv.DictReader(jobs_file)
            for row in jobs_reader:
                self.jobs_list.append(dict(row))
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_jobs = set(row["job_type"] for row in self.jobs_list)
        return list(unique_jobs)

    def filter_by_multiple_criteria(self, jobs, filters) -> List[dict]:
        if not isinstance(filters, dict):
            raise TypeError

        filtered_jobs = []
        for row in jobs:
            if (
                filters["industry"] == row["industry"]
                and filters["job_type"] == row["job_type"]
            ):
                filtered_jobs.append(row)
        return filtered_jobs
