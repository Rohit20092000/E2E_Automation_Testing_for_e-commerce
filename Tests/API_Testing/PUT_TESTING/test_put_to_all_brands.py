from API_CLIENTS.PUT_API.PUT_To_All_Brands_List import put_to_all_brands
import pytest
import json
from jsonschema import validate

@pytest.mark.smoke
def test_put_to_all_brands():
    response = put_to_all_brands.put_to_all_brands_list()
    print("Response Status:", response.status_code)
    print("Response body:", response.text)

    # Parse JSON response
    response_json = response.json()

    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    assert response_json["responseCode"] == 405, f"Expected API responseCode 405, got {response_json['responseCode']}"

    # Load schema
    with open("Schemas/post_to_all_product_list.json") as f:
        schema = json.load(f)

    # Validate response structure
    validate(instance=response_json, schema=schema)
