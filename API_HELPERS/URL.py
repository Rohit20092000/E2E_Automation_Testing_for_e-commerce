class URL:
    base_URL = f"https://automationexercise.com/api"
    @staticmethod
    def get_all_product_url():
        return f"{URL.base_URL}/productsList"
    @staticmethod
    def post_to_all_product_list():
        return f"{URL.base_URL}/productsList"
    @staticmethod
    def get_all_brands_list():
        return f"{URL.base_URL}/brandsList"
    @staticmethod
    def PUT_To_All_Brands_List_Url():
        return f"{URL.base_URL}//brandsList"
    @staticmethod
    def post_to_search_product_url():
        return f"{URL.base_URL}/searchProduct"
    @staticmethod
    def POST_To_Search_Product_without_search_product_parameter():
        return f"{URL.base_URL}/searchProduct"
    @staticmethod
    def post_To_Verify_Login_with_valid_details_url():
        return f"{URL.base_URL}/verifyLogin"
    @staticmethod
    def POST_To_Verify_Login_without_email_parameter_url():
        return f"{URL.base_URL}/verifyLogin"
    #https://automationexercise.com/api/verifyLogin
    @staticmethod
    def DELETE_To_Verify_Login_url():
        return f"{URL.base_URL}/verifyLogin"
    #https://automationexercise.com/api/verifyLogin

    @staticmethod
    def POST_To_Create_Register_User_Account_url():
        # https://automationexercise.com/api/createAccount
        return f"{URL.base_URL}/createAccount"
    @staticmethod
    def DELETE_METHOD_To_Delete_User_Account_url():
        return f"{URL.base_URL}/deleteAccount"
    @staticmethod
    def PUT_METHOD_To_Update_User_Account():
        return f"{URL.base_URL}/updateAccount"
    @staticmethod
    def GET_user_account_detail_by_email_url():
        return f"{URL.base_URL}/getUserDetailByEmail"
    #https://automationexercise.com/api/getUserDetailByEmail
