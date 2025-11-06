from API_HELPERS.URL import URL
from API_HELPERS.headers import Headers
from API_HELPERS.response import RequestHandler
from API_HELPERS.params import Params



class POST_To_Search_Product_without_parameter:
    @staticmethod
    def POST_To_Search_Product_without_search_product_parameter():
        url = URL.POST_To_Search_Product_without_search_product_parameter()
        headers = Headers.get_headers()
        #param = Params.post_to_search_product_param()
        response = RequestHandler.send_post_request(url=url,headers =headers,payload=None,params=None)
        return response
