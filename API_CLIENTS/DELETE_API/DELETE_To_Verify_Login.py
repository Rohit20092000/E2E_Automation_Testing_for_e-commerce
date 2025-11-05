from API_HELPERS.URL import URL
from API_HELPERS.headers import Headers
from API_HELPERS.response import RequestHandler

class DELETE_To_Verify_Login_class:
    @staticmethod
    def DELETE_To_Verify_Login():
        url = URL.DELETE_To_Verify_Login_url()
        headers  = Headers.get_headers()
        response = RequestHandler.delete_request(url,headers,params=None,payload=None)
        return response