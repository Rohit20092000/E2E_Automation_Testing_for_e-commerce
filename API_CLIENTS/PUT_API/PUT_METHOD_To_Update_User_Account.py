from API_HELPERS.URL import URL
from API_HELPERS.headers import Headers
from API_HELPERS.response import RequestHandler
from API_HELPERS.params import Params


class PUT_METHOD_To_Update_User_Account_class:
    @staticmethod
    def PUT_METHOD_To_Update_User_Account(name,email,password,title,birth_date,birth_month,birth_year,firstname,lastname,company,address1,address2,country,zipcode,state,city,mobile_number):
        url = URL.PUT_METHOD_To_Update_User_Account()
        params = Params.POST_To_Create_Register_User_Account_params(name,email,password,title,birth_date,birth_month,birth_year,firstname,lastname,company,address1,address2,country,zipcode,state,city,mobile_number)
        headers = Headers.get_headers()
        response = RequestHandler.send_put_request(url, headers, params=params)
        return response