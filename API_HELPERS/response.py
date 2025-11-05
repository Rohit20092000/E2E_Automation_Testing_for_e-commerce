import requests

class RequestHandler:
    @staticmethod
    def send_post_request(url, headers, payload=None, params=None, as_json=True):
        """
        Sends a POST request with optional params and payload.
        If as_json=True, payload is sent as JSON body.
        """
        if as_json:
            response = requests.post(url, headers=headers, params=params, json=payload)
        else:
            response = requests.post(url, headers=headers, params=params, data=payload)

        return response

    @staticmethod
    def send_post_request_1(url, headers=None, payload=None, params=None, as_json=True):

        if as_json:
                # ✅ JSON body only
            response = requests.post(url, headers=headers, json=payload, params=params)
        else:
                # ✅ Form data body only
            response = requests.post(url, headers=headers, data=payload, params=params)

        return response

    @staticmethod
    def send_get_request(url, headers, params=None, payload=None):
        response = requests.get(url, headers=headers, params=params, json=payload)
        return response
    @staticmethod
    def send_put_request(url,headers,params = None,payload = None):
        response = requests.put(url,headers=headers,params=params,json=payload)
        return response



    @staticmethod
    def delete_request(url, headers, params=None, payload=None):
        response = requests.delete(url, headers=headers, params=params, json=payload)
        return response