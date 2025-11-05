from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.params import Params
from API_HELPERS.headers import Headers


class GET_user_account_detail_by_email_class:
    @staticmethod
    def GET_user_account_detail_by_email(email):
        url = URL.GET_user_account_detail_by_email_url()
        param = Params.GET_user_account_detail_by_email_param(email=email)
        headers = Headers.get_headers()
        response =  RequestHandler.send_get_request(url,headers,params=param,payload=None)
        return response
