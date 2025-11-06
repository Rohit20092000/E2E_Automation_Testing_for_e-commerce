from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.params import Params
from API_HELPERS.headers import Headers

class post_To_Verify_Login_with_valid_details_class:
    @staticmethod
    def test_post_To_Verify_Login_with_valid_details(email,password,payload = None):
        url = URL.post_To_Verify_Login_with_valid_details_url()
        params = Params.post_To_Verify_Login_with_valid_details_param(email,password)
        headers = Headers.get_headers()
        response = RequestHandler.send_post_request(url, headers,payload, params = params)
        return response