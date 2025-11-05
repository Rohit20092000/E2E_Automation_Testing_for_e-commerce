from API_HELPERS.URL import URL
from API_HELPERS.headers import Headers
from API_HELPERS.params import Params
from API_HELPERS.response import RequestHandler

class POST_To_Verify_Login_without_email_parameter_class:
    @staticmethod
    def POST_To_Verify_Login_without_email_parameter(password,payload = None):
        url = URL.POST_To_Verify_Login_without_email_parameter_url()
        params = Params.POST_To_Verify_Login_without_email_parameter_params(password)
        headers = Headers.get_headers()
        response = RequestHandler.send_post_request(url,params,headers)
        return response