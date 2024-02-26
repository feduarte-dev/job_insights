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
        if valid_salaries:
            highest_salary = max(valid_salaries)
            return highest_salary

    def get_min_salary(self) -> int:
        valid_salaries = [
            int(row["min_salary"])
            for row in self.jobs_list
            if row["min_salary"].isnumeric()
        ]
        if valid_salaries:
            lowest_salary = min(valid_salaries)
            return lowest_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
