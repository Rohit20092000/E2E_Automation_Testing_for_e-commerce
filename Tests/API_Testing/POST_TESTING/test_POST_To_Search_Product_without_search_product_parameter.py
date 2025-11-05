from API_CLIENTS.POST_API.POST_To_Search_Product_without_search_product_parameter import POST_To_Search_Product_without_parameter
from jsonschema import validate
import pytest
import json

@pytest.mark.smoke
def test_POST_To_Search_Product_without_parameter():
    response = POST_To_Search_Product_without_parameter.POST_To_Search_Product_without_search_product_parameter()
    print("Status code ",response.status_code)
    print("Response Text",response.text)
    response_json = response.json()

    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    assert response_json["responseCode"] == 400, f"Expected API responseCode 400, got {response_json['responseCode']}"

    # Load schema
    with open("Schemas/post_to_all_product_list.json") as f:
        schema = json.load(f)

    # Validate response structure
    validate(instance=response_json, schema=schema)