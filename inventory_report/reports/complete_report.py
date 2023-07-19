from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self) -> None:
        super().__init__()

    def generate(self) -> str:
        return (
            super().generate()
            + "\n"
            + "Stocked products by company:\n"
            + self.__convert_company_list_with_stocked_products_to_string()
        )

    def __convert_company_list_with_stocked_products_to_string(self) -> str:
        complete_str = ""
        for k, v in self._get_company_list_with_stocked_products():
            complete_str += str(f"- {k}: {v}\n")

        return complete_str
