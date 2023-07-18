import csv
import json
from abc import ABC, abstractmethod
from typing import Dict, List, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path) as file:
            products = json.load(file)
            new_list_products = [Product(**product) for product in products]
        return new_list_products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, encoding="utf-8") as file:
            products = csv.DictReader(file)
            new_list_products = [Product(**product) for product in products]
        return new_list_products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
