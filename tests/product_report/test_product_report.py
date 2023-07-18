from inventory_report.product import Product


def test_product_report() -> None:
    Mock_product_with_all_fields = Product(
        id="1",
        product_name="AI Dev Bot",
        company_name="Developer-machine",
        manufacturing_date="2021-01-01",
        expiration_date="2021-03-31",
        serial_number="123456789",
        storage_instructions="Keep caution! The product could be a fraud",
    )
    assert str(Mock_product_with_all_fields) == (
        "The product 1 - AI Dev Bot "
        + "with serial number 123456789 "
        + "manufactured on 2021-01-01 "
        + "by the company Developer-machine "
        + "valid until 2021-03-31 "
        + "must be stored according to the following instructions: "
        + "Keep caution! The product could be a fraud."
    )
