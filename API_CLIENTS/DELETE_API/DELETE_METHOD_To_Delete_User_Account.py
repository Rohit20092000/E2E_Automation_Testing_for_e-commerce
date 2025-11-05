from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.headers import Headers
from API_HELPERS.params import Params


class DELETE_METHOD_To_Delete_User_Account_class:
    @staticmethod
    def test_DELETE_METHOD_To_Delete_User_Account(email,password):
        url = URL.DELETE_METHOD_To_Delete_User_Account_url()
        params = Params.DELETE_METHOD_To_Delete_User_Account_param(email,password)
        headers  = Headers.get_headers()
        response = RequestHandler.delete_request(url,headers,params =params,payload=None)
        return response