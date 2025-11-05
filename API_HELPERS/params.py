
class Params:
    @staticmethod
    def post_to_all_products_param():
        return{


        }
    @staticmethod
    def post_to_search_product_param(search_product):
        return{
            "search_product": search_product
        }
    @staticmethod
    def post_To_Verify_Login_with_valid_details_param(email,password):
        return {
            "email":email,
            "password":password
        }
    @staticmethod
    def POST_To_Verify_Login_without_email_parameter_params(password):
        return {
            "password":password
        }

    @staticmethod
    def POST_To_Create_Register_User_Account_params(name,email,password,title,birth_date,birth_month,birth_year,firstname,lastname,company,address1,address2,country,zipcode,state,city,mobile_number):
        return {
            "name":name,
            "email":email,
            "password":password,
            "title":title,
            "birth_date":birth_date,
            "birth_month":birth_month,
            "birth_year":birth_year,
            "first_name":firstname,
            "last_name":lastname,
            "company":company,
            "address1":address1,
            "address2":address2,
            "country":country,
            "zipcode":zipcode,
            "state":state,
            "city":city,
            "mobile_number":mobile_number

        }
    @staticmethod
    def DELETE_METHOD_To_Delete_User_Account_param(email,password):
        return {
            "email": email,
            "password": password

        }

    @staticmethod
    def GET_user_account_detail_by_email_param(email):
        return {
            "email": email
        }