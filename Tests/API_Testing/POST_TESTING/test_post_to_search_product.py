from API_CLIENTS.POST_API.post_to_search_product import post_to_search_product_class
import json
import pytest
from jsonschema import validate


@pytest.mark.smoke
def test_post_to_search_product():
    # Make API call with a proper search parameter
    search_product = "top"
    response = post_to_search_product_class.post_to_search_product(params = params,search_product=search_product)

    print("Response status", response.status_code)
    print("Response Text", response.text)

    # Validate HTTP status
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

    response_json = response.json()

    # Load the correct schema for successful search
    with open("Schemas/post_to_search_product_schemas.json") as f:
        schema = json.load(f)

    # Validate response structure
    validate(instance=response_json, schema=schema)
