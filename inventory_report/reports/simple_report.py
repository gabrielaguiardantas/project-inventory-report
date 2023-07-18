from typing import List

from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self._inventory_list: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._inventory_list.append(inventory)

    # def generate(self) -> str:
    #     report = (
    #         "Data de fabricação mais antiga: "
    #         + self._get_earliest_date()
    #         + "\n"
    #         + "Data de validade mais próxima: "
    #         + self._get_closest_expiration_date()
    #         + "\n"
    #         + "Empresa com maior quantidade de produtos estocados: "
    #         + self._get_company_with_most_stocked_products()
    #     )
    #     return report
