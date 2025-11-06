import json
import os

class payloads:
    BASE_PATH = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'

    @staticmethod
    def load_test_data(key="data", index=0):
        """
        Loads test data from JSON file.
        By default, it loads user data from "data" key.
        Example: load_test_data("wrong_data", 0)
        """
        with open(payloads.BASE_PATH, encoding="utf-8") as f:
            data = json.load(f)
        return data[key][index]

    # ------------------------- LOGIN PAYLOAD -------------------------
    @staticmethod
    def build_login_payload(email, password):
        """Builds payload for login API."""
        return {
            "email": email,
            "password": password
        }

    # ------------------------- PRODUCT PAYLOAD -------------------------
    @staticmethod
    def build_product_payload(product_data):
        """Builds payload for product API."""
        return {
            "id": int(product_data["id"]),
            "name": product_data["name"],
            "price": product_data["price"],
            "brand": product_data["brand"],
            "category": {
                "usertype": {"usertype": product_data["usertype"]},
                "category": product_data["category"]
            }
        }

    # ------------------------- REGISTER PAYLOAD -------------------------
    @staticmethod
    def build_register_payload(user_data):
        """Builds payload for registration API."""
        return {
            "name": user_data["name"],
            "email": user_data["email"],
            "password": user_data["password"],
            "address": user_data["address"],
            "city": user_data["city"],
            "state": user_data["state"],
            "zip": user_data["zip_code"],
            "country": user_data["country"],
            "mobile": user_data["Mobile"]
        }
