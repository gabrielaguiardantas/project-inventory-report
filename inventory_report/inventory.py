from typing import List, Union

from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Union[List[Product], None] = None) -> None:
        self._data = [] if data is None else data

    @property
    def data(self) -> List[Product]:
        return self._data

    def add_data(self, data: List[Product]) -> None:
        self._data.extend(data)
