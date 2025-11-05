class Locators:
    login = "//i[@class='fa fa-lock']"
    sign_up_name ="//input[@data-qa='signup-name']"
    sign_up_email = "//input[@data-qa='signup-email']"
    sign_up_button ="//button[@data-qa='signup-button']"
    title ="//input[@id='id_gender1']"
    password = "//input[@type='password']"
    checkbox_1="//input[@id='newsletter']"
    checkbox_2 = "//input[@id='optin']"
    add_name = "//input[@id='first_name']"
    last_name = "//input[@id='last_name']"
    company_name ="//input[@id='company']"
    address = "//input[@id='address1']"
    address_2 = "//input[@id='address2']"
    state_name ="//input[@id='state']"
    city_name ="//input[@id='city']"
    zip_code = "//input[@id='zipcode']"
    Mobile_number ="//input[@id='mobile_number']"
    country = "//select[@id='country']"
    sign_up_for = "//input[@id='newsletter']"
    #DOB
    days = "//select[@id='days']"
    month_select = "//select[@id='months']"
    year_select = "//select[@id='years']"
    create_account_button = "(//button[@type='submit'])[1]"
    Account_creation_message = "//div[@class ='col-sm-9 col-sm-offset-1']"
    continue_button ="//a[text() ='Continue']"
    #test_login_with_correct_password
    login_email ="//input[@data-qa='login-email']"
    submit = "(//button[@type='submit'])[1]"
    email_incorrect_text ="//p[text()='Your email or password is incorrect!']"
    screenshot = "//p[text()='Your email or password is incorrect!']"
    logout =" //a[@href='/logout']"
    successfully_logged_in = "(//a)[11]"

    #Error message with wrong password
    error_message = "//p[text()='Your email or password is incorrect!']"
    # Existing mail message
    existing_email_message = "//p[text()='Email Address already exist!']"

    #Contact Us
    contact_us = "//a[@href='/contact_us']"

    # Delete Account

    delete_account = "//a[@href='/delete_account']"

    #Navigate to Test_cases tab
    navigate_testcase= "//a[@href='/test_cases']"

    #Product_page
    products = "//a[contains(text(),'Products')]"
    categories ="//div[@id='accordian']"
    brands = "//ul[@class='nav nav-pills nav-stacked']"
    women="(//span[@class = 'badge pull-right'])[1]"
    men = "(//span[@class = 'badge pull-right'])[2]"
    kids = "(//span[@class = 'badge pull-right'])[3] "
    dress = "(//a[contains(text(),'Dress')])[1]"
    top = "(//a[contains(text(),'Top')])[1]"
    saree = "(//a[contains(text(),'Saree')])[1]"
    dress_text = "(//h2[contains(text(),'Women - Dress Products')])[1]"
    top_text = "(//h2[contains(text(),'Women - Tops Products')])[1]"
    saree_text = "(//h2[contains(text(),'Women - Saree Products')])[1]"
    tshirt = "(//a[contains(text(),'Tshirts ')])[1]"
    jeans = "(//a[contains(text(),'Jeans ')])[1]"
    tshirt_text = "(//h2[contains(text(),'Men - Tshirts Products')])[1]"
    jeans_text = "(//h2[contains(text(),'Men - Jeans Products')])[1]"
    kids_dress = "(//a[contains(text(),'Dress ')])[2]"
    kids_dress_text  ="//h2[text()='Kids - Dress Products']"
    Tops_Shirts = "//a[text()='Tops & Shirts ']"
    Tops_Shirts_text = "//h2[text()='Kids - Tops & Shirts Products']"

    #search product
    search = "//input[@id='search_product']"
    search_click = "//button[@id='submit_search']"

    #Subscription check
    subscription = "//input[@id='susbscribe_email']"
    subscription_submit = "//button[@id='subscribe']"
    temporary ="//*[contains(text(),'successfully subscribed')]"
    forgot_address = ""

    #add product in cart
    add_first_product = "(//a[@data-product-id='1'])[1]"
    view_cart = "(//a[@href='/view_cart'])[2]"
    proceed = "(//a[text()='Proceed To Checkout'])"
    d_address = "(//ul[@id='address_delivery'])"
    b_address = "(//ul[@id='address_invoice'])"
    remove_from_cart = "//i[@class='fa fa-times']"
    cart_text_after_removing = "(//p[@class='text-center'])[3]"
    return_from_cart = "(//a[@href = '/products'])[2]"

    #download invoice
    first_product ="(//p[contains(@class,'cart_total_price')])[1]"
    second_product = "(//p[contains(@class,'cart_total_price')])[2]"
    total_price = "(//p[contains(@class,'cart_total_price')])[3]"
    comment = "//textarea[@name='message']"
    place_order = "//a[@href='/payment']"
    card_name = "//input[@name='name_on_card']"
    card_number = "//input[@name='card_number']"
    cvc = "//input[@name='cvc']"
    card_expire_month = "//input[@name='expiry_month']"
    card_expire_year = "//input[@name='expiry_year']"
    submit_card_details = "//button[@id='submit']"
    download_invoice = "//a[contains(text(),'Download Invoice')]"

