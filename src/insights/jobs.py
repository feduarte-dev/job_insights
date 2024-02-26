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
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
