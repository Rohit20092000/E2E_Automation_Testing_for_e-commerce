from API_HELPERS.URL import URL
from API_HELPERS.response import RequestHandler
from API_HELPERS.headers import Headers


class put_to_all_brands:
    @staticmethod
    def put_to_all_brands_list():
        url = URL.PUT_To_All_Brands_List_Url()
        headers = Headers.get_headers()
        response = RequestHandler.send_put_request(url,headers,params=None,payload=None)
        return response
