from typing import List, Dict
import csv

jobs = [
    {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
    {"id": 3, "industry": "Finance", "job_type": "FULL_TIME"},
    {"id": 4, "industry": "IT", "job_type": "CONTRACTOR"},
    {"id": 5, "industry": "Healthcare", "job_type": "FULL_TIME"},
    {"id": 6, "industry": "Finance", "job_type": "PART_TIME"},
    {"id": 7, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 8, "industry": "Healthcare", "job_type": "CONTRACTOR"},
]


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
        job_types = []
        for row in self.jobs_list:
            if row["job_type"] not in job_types:
                job_types.append(row["job_type"])
        return job_types

    def filter_by_multiple_criteria(
        self, jobs: list[dict], filters: dict
    ) -> List[dict]:
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
