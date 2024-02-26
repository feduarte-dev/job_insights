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
        try:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])

            if min_salary > max_salary:
                raise ValueError

            return min_salary <= int(salary) <= max_salary
        except (TypeError, KeyError):  # isso é gambiarra?
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_list = []
        for row in jobs:
            try:
                if self.matches_salary_range(row, int(salary)):
                    filtered_list.append(row)
            finally:
                continue
        return filtered_list


# teste = ProcessSalaries()
# teste.read("data/jobs.csv")
# print(teste.matches_salary_range({"max_salary": 10000, "min_salary": 0}, -1))

# para funcionar minhas variaveis preciso corrigir o import
