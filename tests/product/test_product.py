from inventory_report.product import Product


def test_create_product() -> None:
    Mock_product_with_all_fields = Product(
        id="1",
        product_name="AI Dev Bot",
        company_name="Developer-machine",
        manufacturing_date="2021-01-01",
        expiration_date="2021-03-31",
        serial_number="123456789",
        storage_instructions="Keep caution! The product could be a fraud",
    )
    assert Mock_product_with_all_fields.id == "1"
    assert Mock_product_with_all_fields.product_name == "AI Dev Bot"
    assert Mock_product_with_all_fields.company_name == "Developer-machine"
    assert Mock_product_with_all_fields.manufacturing_date == "2021-01-01"
    assert Mock_product_with_all_fields.expiration_date == "2021-03-31"
    assert Mock_product_with_all_fields.serial_number == "123456789"
    assert (
        Mock_product_with_all_fields.storage_instructions
        == "Keep caution! The product could be a fraud"
    )
