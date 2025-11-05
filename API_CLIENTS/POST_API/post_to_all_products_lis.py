from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.headers import Headers

class PostToAllProduct:
    @staticmethod
    def post_to_all_product_list(payload=None, params=None):
        url = URL.post_to_all_product_list()
        headers = Headers.get_headers()
        response = RequestHandler.send_post_request(url, headers, payload=payload, params=params)
        return response
