from jsonschema import validate
import json
import pytest
from API_CLIENTS.PUT_API.PUT_METHOD_To_Update_User_Account import PUT_METHOD_To_Update_User_Account_class

@pytest.mark.smoke
def test_PUT_METHOD_To_Update_User_Account():
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
    response = PUT_METHOD_To_Update_User_Account_class.PUT_METHOD_To_Update_User_Account(name=name,
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
        mobile_number=mobile_number)
    print("Status Code ",response.status_code)
    print("Status Text ",response.text)
    assert response.status_code == 200, f" expected 200 but got {response.status_code}"
