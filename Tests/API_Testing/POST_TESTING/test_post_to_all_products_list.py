from API_CLIENTS.POST_API.post_to_all_products_lis import PostToAllProduct
import pytest
import json
from jsonschema import validate


@pytest.mark.smoke
def test_post_of_all_product_lists():

    response = PostToAllProduct.post_to_all_product_list(payload=None, params=None)
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
