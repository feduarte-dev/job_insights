from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = set(
            row["industry"] for row in self.jobs_list if row["industry"] != ""
        )
        return list(unique_industries)


# teste = ProcessIndustries()
# teste.read("data/jobs.csv")
# print(teste.get_unique_industries())

# para funcionar minhas variaveis preciso corrigir o import
