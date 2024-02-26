from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        highest_salary = 0
        for row in self.jobs_list:
            if (
                row["max_salary"] != ""
                and row["max_salary"] != "invalid"
                and int(row["max_salary"]) > highest_salary
            ):

                highest_salary = int(row["max_salary"])
        return highest_salary

    def get_min_salary(self) -> int:
        lowest_salary = 9999999999999999
        for row in self.jobs_list:
            if (
                row["min_salary"] != ""
                and row["min_salary"] != "invalid"
                and int(row["min_salary"]) < lowest_salary
            ):

                lowest_salary = int(row["min_salary"])
        return lowest_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
