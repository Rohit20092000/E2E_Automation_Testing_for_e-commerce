from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.headers import Headers

class Post_all_brand:
    @staticmethod
    def all_brands_list():
        url = URL.get_all_brands_list()
        headers = Headers.get_headers()
        response = RequestHandler.send_get_request(url,headers,params=None)
        return response