from API_HELPERS.URL import URL
from API_HELPERS.headers import Headers
from API_HELPERS.response import RequestHandler
from API_HELPERS.params import Params


class post_to_search_product_class:
    @staticmethod
    def post_to_search_product(search_product):
        url = URL.post_to_search_product_url()
        params = Params.post_to_search_product_param(search_product)
        headers = Headers.get_headers()
        response = RequestHandler.send_put_request(url,params,headers,payload=None)
        return response