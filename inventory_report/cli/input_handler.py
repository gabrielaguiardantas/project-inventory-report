from typing import List, Union

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    report = verify_report_type(report_type)

    for file_path in file_paths:
        inventory = Inventory()
        if file_path.endswith(".csv"):
            inventory.add_data(CsvImporter(file_path).import_data())
            report.add_inventory(inventory)
        elif file_path.endswith(".json"):
            inventory.add_data(JsonImporter(file_path).import_data())
            report.add_inventory(inventory)
    return report.generate()


def verify_report_type(
    report_type: str,
) -> Union[SimpleReport, CompleteReport]:
    if report_type == "simple":
        return SimpleReport()
    elif report_type == "complete":
        return CompleteReport()
    else:
        raise ValueError("Report type is invalid.")
