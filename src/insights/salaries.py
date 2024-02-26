from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        valid_salaries = [
            int(row["max_salary"])
            for row in self.jobs_list
            if row["max_salary"].isnumeric()
        ]
        return max(valid_salaries)

    def get_min_salary(self) -> int:
        valid_salaries = [
            int(row["min_salary"])
            for row in self.jobs_list
            if row["min_salary"].isnumeric()
        ]
        return min(valid_salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            if int(job["min_salary"]) > int(job["max_salary"]):
                raise ValueError

            return (
                int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
            )
        except (TypeError, KeyError):
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_list = []
        for row in jobs:
            try:
                if self.matches_salary_range(row, salary):
                    filtered_list.append(row)
            except ValueError:
                continue
        return filtered_list
