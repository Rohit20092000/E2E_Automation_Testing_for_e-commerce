
import pytest
from API_CLIENTS.GET_API.Get_all_product_list import get_all_products
import json
from jsonschema import validate


@pytest.mark.smoke
def test_get_all_product_list():
    response = get_all_products.get_all_product_list()
    print("Status code ",response.status_code)
    print("Response body", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/get_all_product_list_schemas.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")

