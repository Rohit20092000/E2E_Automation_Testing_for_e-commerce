import json
import pytest
from jsonschema import validate
from API_CLIENTS.POST_API.POST_To_Create_Register_User_Account import POST_To_Create_Register_User_Account_class

@pytest.mark.smoke
def test_POST_To_Create_Register_User_Account():
    # Input data (these simulate registration fields)
    name = "Rohit"
    email = "sa40086305@gmail.com"
    password = "Rohit_juyal"
    title = "Mr"
    birth_date = "29"
    birth_month = "August"
    birth_year = "2000"
    firstname = "Rohit"
    lastname = "Juyal"
    company = "Wipro"
    address1 = "satichaur"
    address2 = "Kotdwar"
    country = "India"
    zipcode = "248007"
    state = "Uttarakhand"
    city = "Kotdwar"
    mobile_number = "9027607045"

    # Call the API
    response = POST_To_Create_Register_User_Account_class.POST_To_Create_Register_User_Account(
        name=name,
        email=email,
        password=password,
        title=title,
        birth_date=birth_date,
        birth_month=birth_month,
        birth_year=birth_year,
        firstname=firstname,
        lastname=lastname,
        company=company,
        address1=address1,
        address2=address2,
        country=country,
        zipcode=zipcode,
        state=state,
        city=city,
        mobile_number=mobile_number
    )

    print("Status code:", response.status_code)
    print("Response Text:", response.text)

    # Ensure HTTP response code is 200 (OK)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

    # Parse JSON response
    response_json = response.json()

    # Load JSON Schema
    with open("Schemas/POST_To_Create_Register_User_Account_schemas.json") as f:
        schema = json.load(f)

    # Validate JSON body
    validate(instance=response_json, schema=schema)
