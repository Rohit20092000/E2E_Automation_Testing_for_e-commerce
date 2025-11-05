from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.headers import Headers

class get_all_products:
    @staticmethod
    def get_all_product_list(payload = None):
        url = URL.get_all_product_url()
        headers = Headers.get_headers()
        response = RequestHandler.send_get_request(url,headers,payload = payload)
        return response