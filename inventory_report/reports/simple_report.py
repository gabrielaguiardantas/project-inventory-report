from datetime import date
from typing import List, Tuple

from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self._inventory_list: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._inventory_list.append(inventory)

    def generate(self) -> str:
        (
            company_name,
            total_stocked,
        ) = self._get_company_list_with_stocked_products()[0]
        report = (
            "Oldest manufacturing date: "
            + self._get_oldest_date()
            + "\n"
            + "Closest expiration date: "
            + self._get_closest_expiration_date()
            + "\n"
            + "Company with the largest inventory: "
            + company_name
        )
        return report

    def _get_oldest_date(self) -> str:
        oldest_date = self._inventory_list[0].data[0].manufacturing_date
        for inventory in self._inventory_list:
            for product in inventory.data:
                # bigger date comes after smaller date
                if product.manufacturing_date < oldest_date:
                    oldest_date = product.manufacturing_date
        return oldest_date

    def _get_closest_expiration_date(self) -> str:
        future_expiration_date_list = []
        for inventory in self._inventory_list:
            for product in inventory.data:
                if product.expiration_date > str(date.today()):
                    future_expiration_date_list.append(product.expiration_date)
        return min(future_expiration_date_list)

    def _get_company_list_with_stocked_products(
        self,
    ) -> List[Tuple[str, int]]:
        company_name_frequency_dict: dict[str, int] = {}
        for inventory in self._inventory_list:
            for product in inventory.data:
                company_name_frequency_dict[product.company_name] = (
                    company_name_frequency_dict.get(product.company_name, 0)
                    + 1
                )
        ordered_company_name_frequency_list = sorted(
            company_name_frequency_dict.items(),
            reverse=True,
            key=lambda x: x[1],
        )
        return ordered_company_name_frequency_list
