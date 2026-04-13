from playwright.sync_api import Page, expect

""" API 1: Get All Products List
        API URL: https://automationexercise.com/api/productsList
        Request Method: GET
        Response Code: 200
        Response JSON: All products list
"""
def test1(page: Page):
    page.goto("https://playwright.dev/")
    

""" API 2: POST To All Products List
        API URL: https://automationexercise.com/api/productsList
        Request Method: POST
        Response Code: 405
        Response Message: This request method is not supported.
"""
def test2(page: Page):
    page.goto("https://playwright.dev/")


""" API 3: Get All Brands List
        API URL: https://automationexercise.com/api/brandsList
        Request Method: GET
        Response Code: 200
        Response JSON: All brands list
"""
def test3(page: Page):
    page.goto("https://playwright.dev/")


""" API 4: PUT To All Brands List
        API URL: https://automationexercise.com/api/brandsList
        Request Method: PUT
        Response Code: 405
        Response Message: This request method is not supported.
"""
def test4(page: Page):
    page.goto("https://playwright.dev/")


""" API 5: POST To Search Product
        API URL: https://automationexercise.com/api/searchProduct
        Request Method: POST
        Request Parameter: search_product (For example: top, tshirt, jean)
        Response Code: 200
        Response JSON: Searched products list
"""
def test5(page: Page):
    page.goto("https://playwright.dev/")



""" API 6: POST To Search Product without search_product parameter
        API URL: https://automationexercise.com/api/searchProduct
        Request Method: POST
        Response Code: 400
        Response Message: Bad request, search_product parameter is missing in POST request.
"""
def test6(page: Page):
    page.goto("https://playwright.dev/")



""" API 7: POST To Verify Login with valid details
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        Request Parameters: email, password
        Response Code: 200
        Response Message: User exists!
"""
def test7(page: Page):
    page.goto("https://playwright.dev/")



""" API 8: POST To Verify Login without email parameter
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        Request Parameter: password
        Response Code: 400
        Response Message: Bad request, email or password parameter is missing in POST request.
"""
def test8(page: Page):
    page.goto("https://playwright.dev/")



""" API 9: DELETE To Verify Login
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: DELETE
        Response Code: 405
        Response Message: This request method is not supported.
"""
def test9(page: Page):
    page.goto("https://playwright.dev/")



""" API 10: POST To Verify Login with invalid details
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        Request Parameters: email, password (invalid values)
        Response Code: 404
        Response Message: User not found!
"""
def test10(page: Page):
    page.goto("https://playwright.dev/")



""" API 11: POST To Create/Register User Account
        API URL: https://automationexercise.com/api/createAccount
        Request Method: POST
        Request Parameters: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
        Response Code: 201
        Response Message: User created!
"""
def test11(page: Page):
    page.goto("https://playwright.dev/")



""" API 12: DELETE METHOD To Delete User Account
        API URL: https://automationexercise.com/api/deleteAccount
        Request Method: DELETE
        Request Parameters: email, password
        Response Code: 200
        Response Message: Account deleted!
"""
def test12(page: Page):
    page.goto("https://playwright.dev/")



""" API 13: PUT METHOD To Update User Account
        API URL: https://automationexercise.com/api/updateAccount
        Request Method: PUT
        Request Parameters: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
        Response Code: 200
        Response Message: User updated!
"""
def test13(page: Page):
    page.goto("https://playwright.dev/")



""" API 14: GET user account detail by email
        API URL: https://automationexercise.com/api/getUserDetailByEmail
        Request Method: GET
        Request Parameters: email
        Response Code: 200
        Response JSON: User Detail
"""
def test14(page: Page):
    page.goto("https://playwright.dev/")


