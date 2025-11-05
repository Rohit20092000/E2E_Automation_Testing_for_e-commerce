import json
import pytest
from API_CLIENTS.GET_API.Get_All_Brands_List import Post_all_brand
from jsonschema import validate

@pytest.mark.smoke
def test_get_all_product_list():
    response = Post_all_brand.all_brands_list()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/get_all_brands_list_schemas.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")

