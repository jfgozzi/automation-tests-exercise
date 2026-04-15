from playwright.sync_api import Page, expect, Browser
from utils import check, create_user
import random
import re

""" Test Case 1: Register User
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and email address
        7. Click 'Signup' button
        8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        9. Fill details: Title, Name, Email, Password, Date of birth
        10. Select checkbox 'Sign up for our newsletter!'
        11. Select checkbox 'Receive special offers from our partners!'
        12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        13. Click 'Create Account button'
        14. Verify that 'ACCOUNT CREATED!' is visible
        15. Click 'Continue' button
        16. Verify that 'Logged in as username' is visible
        17. Click 'Delete Account' button
        18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
"""
def test1(page: Page):
    page.goto("https://automationexercise.com")

    expect(page).to_have_title("Automation Exercise")

    page.get_by_role("link", name="Signup / Login").click()
    
    signup_heading = page.get_by_role("heading", name="New User Signup!")
    expect(signup_heading).to_be_visible()

    page.get_by_placeholder("Name").fill("Juan")
    
    # ver el porque de este
    page.locator(".signup-form [data-qa='signup-email']").fill("testmail111112@gmail.com")

    page.get_by_role("button", name="Signup").click()

    expect(page.get_by_text("ENTER ACCOUNT INFORMATION")).to_be_visible()

    page.get_by_label("Mr.").click()

    page.get_by_label("Sign up for our newsletter!").click()
    page.get_by_label("Receive special offers from our partners!").click()


    page.get_by_label("Password").fill("hello1234")

    page.select_option('#days', '1')
    page.select_option('#months', '12')
    page.select_option('#years', '2000')

    page.locator("#first_name").fill("hello")
    page.locator("#last_name").fill("goodbye")
    page.locator("#company").fill("fakeCompany")
    page.locator("#address1").fill("fakeStreet")
    page.locator("#address2").fill("fakeStreet2")

    page.select_option('#country', 'United States')

    page.locator("#state").fill("Connecticut")
    page.locator("#city").fill("Bristol")
    page.locator("#zipcode").fill("1234")
    page.locator("#mobile_number").fill("12345678")

    page.get_by_role("button", name="Create Account").click()
    
    expect(page.get_by_role("heading", name="ACCOUNT CREATED!", exact=False)).to_be_visible()
    
    page.get_by_role("link", name="Continue").click()

    expect(page.get_by_text("Logged in as Juan")).to_be_visible()

    page.get_by_role("link", name="Delete Account").click()

    expect(page.get_by_role("heading", name="ACCOUNT DELETED!", exact=False)).to_be_visible()

    page.get_by_role("link", name="Continue").click()


    
""" Test Case 2: Login User with correct email and password
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Delete Account' button
        10. Verify that 'ACCOUNT DELETED!' is visible
"""
def test2(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    #signup_heading = page.get_by_role("heading", name="Login to your account")
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    
    page.locator(".login-form [data-qa='login-email']").fill("maildeprueba12345@gmail.com")
    page.get_by_placeholder("Password").fill("hola123")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Logged in as Juan")).to_be_visible()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_role("heading", name="ACCOUNT DELETED!", exact=False)).to_be_visible()

    
    
""" Test Case 3: Login User with incorrect email and password
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter incorrect email address and password
        7. Click 'login' button
        8. Verify error 'Your email or password is incorrect!' is visible
"""
def test3(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    page.locator(".login-form [data-qa='login-email']").fill("mailtest@gmail.com")
    page.get_by_placeholder("Password").fill("12")  
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()



""" Test Case 4: Logout User
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Logout' button
        10. Verify that user is navigated to login page
"""
def test4(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    page.locator(".login-form [data-qa='login-email']").fill("maildeprueba12345@gmail.com")
    page.get_by_placeholder("Password").fill("hola1234")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Logged in as Juan")).to_be_visible()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_title("Automation Exercise - Signup / Login")



""" Test Case 5: Register User with existing email
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and already registered email address
        7. Click 'Signup' button
        8. Verify error 'Email Address already exist!' is visible
"""
def test5(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()
    page.get_by_placeholder("Name").fill("Juan")
    page.locator(".signup-form [data-qa='signup-email']").fill("maildeprueba12345@gmail.com")
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()



""" Test Case 6: Contact Us Form
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Contact Us' button
        5. Verify 'GET IN TOUCH' is visible
        6. Enter name, email, subject and message
        7. Upload file
        8. Click 'Submit' button
        9. Click OK button
        10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        11. Click 'Home' button and verify that landed to home page successfully
"""
def test6(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")   
    page.get_by_role("link", name="Contact us").click()
    expect(page.get_by_role("heading", name="GET IN TOUCH")).to_be_visible()
    page.get_by_placeholder("Name").fill("Juan")
    page.get_by_placeholder("Email", exact=True).fill("tu_mail@test.com")    
    page.get_by_placeholder("Subject").fill("Subject")
    page.get_by_placeholder("Message").fill("Message")

    page.set_input_files('input[name="upload_file"]', "/Users/juangozzi/Documents/Proyectos/automation-tests-exsercise/automation-tests-exercise/ui/file.txt")

    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Submit").click()
    expect(page.locator(".status.alert-success")).to_be_visible()    
    page.get_by_role("link", name="Home").nth(1).click()



""" Test Case 7: Verify Test Cases Page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Test Cases' button
        5. Verify user is navigated to test cases page successfully
"""
def test7(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")  
    page.get_by_role("link", name="Test Cases").nth(0).click()
    if "#google_vignette" in page.url:
        page.goto("https://automationexercise.com/test_cases")
    expect(page.locator("h2:has-text('Test Cases')")).to_be_visible()



""" Test Case 8: Verify All Products and product detail page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Products' button
        5. Verify user is navigated to ALL PRODUCTS page successfully
        6. The products list is visible
        7. Click on 'View Product' of first product
        8. User is landed to product detail page
        9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
"""
def test8(page: Page):
    page.goto("https://automationexercise.com")
    if "#google_vignette" in page.url:
        page.goto("https://automationexercise.com/test_cases")
    expect(page).to_have_title("Automation Exercise")  
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_title("Automation Exercise - All Products")
    expect(page.locator(".features_items")).to_be_visible()
    page.get_by_role("link", name="View Product").nth(0).click()
    expect(page.locator(".product-details")).to_be_visible()    
    expect(page.locator(".product-information h2")).to_be_visible()
    expect(page.get_by_text("Category:")).to_be_visible()
    expect(page.get_by_text("Rs.")).to_be_visible()
    expect(page.get_by_text("Availability:")).to_be_visible()
    expect(page.get_by_text("Condition:")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()



""" Test Case 9: Search Product
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Products' button
        5. Verify user is navigated to ALL PRODUCTS page successfully
        6. Enter product name in search input and click search button
        7. Verify 'SEARCHED PRODUCTS' is visible
        8. Verify all the products related to search are visible
"""
def test9(page: Page):
    page.goto("https://automationexercise.com")
    if "#google_vignette" in page.url:
        page.goto("https://automationexercise.com/test_cases")
    expect(page).to_have_title("Automation Exercise")  
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_title("Automation Exercise - All Products")
    product = "Premium Polo T-Shirts"
    page.get_by_placeholder("Search Product").fill(product)
    page.locator("#submit_search").click()
    expect(page.locator("h2:has-text('Searched Products')")).to_be_visible()

    nombres_productos = page.locator(".productinfo p")
    items = nombres_productos.all()
    for item in items:
        expect(item).to_be_visible()
        expect(item).to_contain_text("Polo", ignore_case=True)   



""" Test Case 10: Verify Subscription in home page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Scroll down to footer
        5. Verify text 'SUBSCRIPTION'
        6. Enter email address in input and click arrow button
        7. Verify success message 'You have been successfully subscribed!' is visible
"""
def test10(page: Page):
    check(page)
    page.get_by_text("Subscription").scroll_into_view_if_needed()
    expect(page.locator("h2:has-text('Subscription')")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("somefeikymail@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed!")).to_be_visible()



""" Test Case 11: Verify Subscription in Cart page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click 'Cart' button
        5. Scroll down to footer
        6. Verify text 'SUBSCRIPTION'
        7. Enter email address in input and click arrow button
        8. Verify success message 'You have been successfully subscribed!' is visible
"""
def test11(page: Page):
    check(page)
    page.get_by_role("link", name="Cart").click()
    page.get_by_text("Subscription").scroll_into_view_if_needed()
    expect(page.locator("h2:has-text('Subscription')")).to_be_visible()
    page.get_by_placeholder("Your email address").fill("somefeikymail@gmail.com")
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully subscribed!")).to_be_visible()



""" Test Case 12: Add Products in Cart
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click 'Products' button
        5. Hover over first product and click 'Add to cart'
        6. Click 'Continue Shopping' button
        7. Hover over second product and click 'Add to cart'
        8. Click 'View Cart' button
        9. Verify both products are added to Cart
        10. Verify their prices, quantity and total price
"""
def test12(page: Page):
    check(page)
    page.get_by_role("link", name="Products").click()

    first_prod = page.locator(".single-products").nth(0)
    first_prod.hover()
    first_prod.locator(".overlay-content .add-to-cart").click()

    page.get_by_role("button", name="Continue Shopping").click()   

    second_prod = page.locator(".single-products").nth(1)
    second_prod.hover()
    second_prod.locator(".overlay-content .add-to-cart").click()

    page.get_by_role("link", name="View Cart").click()   

    products = page.locator("tbody tr")
    expect(products).to_have_count(2)

    p1 = products.nth(0)
    expect(p1.locator(".cart_price")).to_contain_text("Rs. 500")
    expect(p1.locator(".cart_quantity")).to_have_text("1")
    expect(p1.locator(".cart_total")).to_contain_text("Rs. 500")
    
    
    p2 = products.nth(1)
    expect(p2.locator(".cart_price")).to_contain_text("Rs. 400")
    expect(p2.locator(".cart_quantity")).to_have_text("1")
    expect(p2.locator(".cart_total")).to_contain_text("Rs. 400")



""" Test Case 13: Verify Product quantity in Cart
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click 'View Product' for any product on home page
        5. Verify product detail is opened
        6. Increase quantity to 4
        7. Click 'Add to cart' button
        8. Click 'View Cart' button
        9. Verify that product is displayed in cart page with exact quantity
"""
def test13(page: Page):
    check(page)
    idx = random.randint(0, 32)
    page.get_by_text("View Product").nth(idx).click()
    
    expect(page.locator(".product-details")).to_be_visible()    
    expect(page.locator(".product-information h2")).to_be_visible()
    expect(page.get_by_text("Category:")).to_be_visible()
    expect(page.get_by_text("Rs.")).to_be_visible()
    expect(page.get_by_text("Availability:")).to_be_visible()
    expect(page.get_by_text("Condition:")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()
    page.locator("#quantity").fill("4")



""" Test Case 14: Place Order: Register while Checkout
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4.ddress Deta Add products to cart
        5. Click 'Cart' button
        6. Verify that cart page is displayed
        7. Click Proceed To Checkout
        8. Click 'Register / Login' button
        9. Fill all details in Signup and create account
        10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        11. Verify ' Logged in as username' at top
        12. Click 'Cart' button
        13. Click 'Proceed To Checkout' button
        14. Verify Ails and Review Your Order
        15. Enter description in comment text area and click 'Place Order'
        16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
        17. Click 'Pay and Confirm Order' button
        18. Verify success message 'Your order has been placed successfully!'
        19. Click 'Delete Account' button
        20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""
def test14(page: Page):
    check(page)

    collected = set()
    for i in range(0, 2):
        idx = random.randint(0, 32)
        while idx in collected:
            idx = random.randint(0, 32)
        collected.add(idx)
        prod = page.locator(".single-products").nth(idx)
        prod.scroll_into_view_if_needed()
        prod.hover()
        prod.locator(".overlay-content .add-to-cart").click()
        page.get_by_role("button", name="Continue Shopping").click()

    page.get_by_role("link", name="Cart").click()
    expect(page.locator("tbody tr")).to_have_count(2)
    page.get_by_text("Proceed To Checkout").click()
    page.locator("#checkoutModal").get_by_role("link", name="Register / Login").click()

    data_user = create_user(page)
    page.get_by_role("link", name="Cart").click()
    page.locator(".check_out").click()

    expect(page.locator("#address_delivery .address_firstname")).to_contain_text(data_user["name"], ignore_case=True)
    expect(page.locator("#address_delivery").locator(".address_address1").nth(1)).to_contain_text(data_user["name"])
    
    combined_line = page.locator("#address_delivery").locator(".address_city")
    expect(combined_line).to_contain_text(data_user["name"])
    expect(combined_line).to_contain_text(data_user["name"])
    expect(combined_line).to_contain_text(data_user["name"])

    page.locator("textarea[name='message']").fill("No comments.")
    page.get_by_role("link", name="Place Order").click()

    page.locator("[data-qa='name-on-card']").fill(data_user["name"])
    page.locator("[data-qa='card-number']").fill(data_user["card_number"]) 
    page.locator("[data-qa='cvc']").fill(data_user["card_cvv"])
    page.locator("[data-qa='expiry-month']").fill(data_user["card_expire"].split("/")[0])
    page.locator("[data-qa='expiry-year']").fill(data_user["card_expire"].split("/")[1])
    page.locator("#submit").click()
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_role("heading", name="ACCOUNT DELETED!", exact=False)).to_be_visible()


""" Test Case 15: Place Order: Register before Checkout
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click 'Signup / Login' button
        5. Fill all details in Signup and create account
        6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        7. Verify ' Logged in as username' at top
        8. Add products to cart
        9. Click 'Cart' button
        10. Verify that cart page is displayed
        11. Click Proceed To Checkout
        12. Verify Address Details and Review Your Order
        13. Enter description in comment text area and click 'Place Order'
        14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
        15. Click 'Pay and Confirm Order' button
        16. Verify success message 'Your order has been placed successfully!'
        17. Click 'Delete Account' button
        18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""
def test15(page: Page):
    check(page)
    page.get_by_role("link", name="Signup / Login").click()
    data_user = create_user(page)

    collected = set()
    for i in range(0, 2):
        idx = random.randint(0, 32)
        while idx in collected:
            idx = random.randint(0, 32)
        collected.add(idx)
        prod = page.locator(".single-products").nth(idx)
        prod.scroll_into_view_if_needed()
        prod.hover()
        prod.locator(".overlay-content .add-to-cart").click()
        page.get_by_role("button", name="Continue Shopping").click()
    
    page.get_by_role("link", name="Cart").click()
    expect(page.locator("tbody tr")).to_have_count(2)
    page.get_by_text("Proceed To Checkout").click()

    expect(page.locator("#address_delivery .address_firstname")).to_contain_text(data_user["name"], ignore_case=True)
    expect(page.locator("#address_delivery").locator(".address_address1").nth(1)).to_contain_text(data_user["name"])
    
    combined_line = page.locator("#address_delivery").locator(".address_city")
    expect(combined_line).to_contain_text(data_user["name"])
    expect(combined_line).to_contain_text(data_user["name"])
    expect(combined_line).to_contain_text(data_user["name"])

    page.locator("textarea[name='message']").fill("No comments.")
    page.get_by_role("link", name="Place Order").click()

    page.locator("[data-qa='name-on-card']").fill(data_user["name"])
    page.locator("[data-qa='card-number']").fill(data_user["card_number"]) 
    page.locator("[data-qa='cvc']").fill(data_user["card_cvv"])
    page.locator("[data-qa='expiry-month']").fill(data_user["card_expire"].split("/")[0])
    page.locator("[data-qa='expiry-year']").fill(data_user["card_expire"].split("/")[1])
    page.locator("#submit").click()
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_role("heading", name="ACCOUNT DELETED!", exact=False)).to_be_visible()


""" Test Case 16: Place Order: Login before Checkout
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click 'Signup / Login' button
        5. Fill email, password and click 'Login' button
        6. Verify 'Logged in as username' at top
        7. Add products to cart
        8. Click 'Cart' button
        9. Verify that cart page is displayed
        10. Click Proceed To Checkout
        11. Verify Address Details and Review Your Order
        12. Enter description in comment text area and click 'Place Order'
        13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
        14. Click 'Pay and Confirm Order' button
        15. Verify success message 'Your order has been placed successfully!'
        16. Click 'Delete Account' button
        17. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""
def test16(browser): 
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://automationexercise.com/login")
    data_user = create_user(page1) 
    context1.close()
    context2 = browser.new_context()
    page = context2.new_page()
    page.goto("https://automationexercise.com/login")
    page.locator(".login-form [data-qa='login-email']").fill(data_user["email"])
    page.locator(".login-form [data-qa='login-password']").fill(data_user["password"])
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text(f"Logged in as {data_user['name']}")).to_be_visible()

    collected = set()
    for i in range(0, 2):
        idx = random.randint(0, 32)
        while idx in collected:
            idx = random.randint(0, 32)
        collected.add(idx)
        prod = page.locator(".single-products").nth(idx)
        prod.scroll_into_view_if_needed()
        prod.hover()
        prod.locator(".overlay-content .add-to-cart").click()
        page.get_by_role("button", name="Continue Shopping").click()

    page.get_by_role("link", name="Cart").click()
    expect(page.locator("tbody tr")).to_have_count(2)
    page.get_by_text("Proceed To Checkout").click()
    expect(page.locator("#address_delivery .address_firstname")).to_contain_text(data_user["name"], ignore_case=True)
    expect(page.locator("#address_delivery").locator(".address_address1").nth(1)).to_contain_text(data_user["name"])
    
    combined_line = page.locator("#address_delivery").locator(".address_city")
    expect(combined_line).to_contain_text(data_user["name"])
    expect(combined_line).to_contain_text(data_user["name"])
    expect(combined_line).to_contain_text(data_user["name"])

    page.locator("textarea[name='message']").fill("No comments.")
    page.get_by_role("link", name="Place Order").click()

    page.locator("[data-qa='name-on-card']").fill(data_user["name"])
    page.locator("[data-qa='card-number']").fill(data_user["card_number"]) 
    page.locator("[data-qa='cvc']").fill(data_user["card_cvv"])
    page.locator("[data-qa='expiry-month']").fill(data_user["card_expire"].split("/")[0])
    page.locator("[data-qa='expiry-year']").fill(data_user["card_expire"].split("/")[1])
    page.locator("#submit").click()
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_role("heading", name="ACCOUNT DELETED!", exact=False)).to_be_visible()     



""" Test Case 17: Remove Products From Cart
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Add products to cart
        5. Click 'Cart' button
        6. Verify that cart page is displayed
        7. Click 'X' button corresponding to particular product
        8. Verify that product is removed from the cart
"""
def test17(page: Page):
    check(page)
    collected = set()
    for i in range(0, 2):
        idx = random.randint(0, 32)
        while idx in collected:
            idx = random.randint(0, 32)
        collected.add(idx)
        prod = page.locator(".single-products").nth(idx)
        prod.scroll_into_view_if_needed()
        prod.hover()
        prod.locator(".overlay-content .add-to-cart").click()
        page.get_by_role("button", name="Continue Shopping").click()

    page.get_by_role("link", name="Cart").click()
    expect(page.locator("tbody tr")).to_have_count(2)

    cart_rows = page.locator("tbody tr")
    total_items = cart_rows.count()
    random_index = random.randint(0, total_items - 1)
    target_row = cart_rows.nth(random_index)
    target_row.locator(".cart_quantity_delete").click()
    expect(target_row).to_be_hidden()



""" Test Case 18: View Category Products
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that categories are visible on left side bar
        4. Click on 'Women' category
        5. Click on any category link under 'Women' category, for example: Dress
        6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
        7. On left side bar, click on any sub-category link of 'Men' category
        8. Verify that user is navigated to that category page
"""
def test18(page: Page): # hacer dinámico
    check(page)
    expect(page.locator("h2:has-text('Category')")).to_be_visible()

    page.locator("#accordian").get_by_role("link", name="Women").click()
    page.get_by_role("link", name="Dress").click()
    expect(page.locator("h2:has-text('Women - Dress Products')")).to_be_visible()

    page.locator("a[href='#Men']").click()
    page.get_by_role("link", name="Jeans").click()
    expect(page.locator("h2:has-text('Men - Jeans Products')")).to_be_visible()



""" Test Case 19: View & Cart Brand Products
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Click on 'Products' button
        4. Verify that Brands are visible on left side bar
        5. Click on any brand name
        6. Verify that user is navigated to brand page and brand products are displayed
        7. On left side bar, click on any other brand link
        8. Verify that user is navigated to that brand page and can see products
"""
def test19(page: Page): 
    check(page)
    page.get_by_role("link", name="Products").click()
    expect(page.locator(".brands_products")).to_be_visible()
    page.get_by_role("link", name="Polo").click() # hacer dinamico
    expect(page.locator("h2:has-text('Brand - Polo Products')")).to_be_visible()
    expect(page).to_have_url(re.compile(rf".*/brand_products/Polo"))
    expect(page.locator("h2.title")).to_contain_text("BRAND - POLO PRODUCTS", ignore_case=True)
    productos_renderizados = page.locator(".single-products")
    expect(productos_renderizados.first).to_be_visible()



""" Test Case 20: Search Products and Verify Cart After Login
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Click on 'Products' button
        4. Verify user is navigated to ALL PRODUCTS page successfully
        5. Enter product name in search input and click search button
        6. Verify 'SEARCHED PRODUCTS' is visible
        7. Verify all the products related to search are visible
        8. Add those products to cart
        9. Click 'Cart' button and verify that products are visible in cart
        10. Click 'Signup / Login' button and submit login details
        11. Again, go to Cart page
        12. Verify that those products are visible in cart after login as well
"""
def test20(page: Page):
    check(page)
    page.get_by_role("link", name="Products").click()
    expect(page.locator("h2:has-text('All Products')")).to_be_visible()
    expect(page).to_have_url(re.compile(rf".*/products"))
    productos_renderizados = page.locator(".single-products")
    expect(productos_renderizados.first).to_be_visible()
    product = page.locator(".single-products p").first.inner_text()
    page.get_by_placeholder("Search Product").fill(product)
    page.locator("#submit_search").click()
    expect(page.locator("h2:has-text('SEARCHED PRODUCT')")).to_be_visible()
    actual = page.locator(".single-products p").first.inner_text()
    assert actual == product # ??
    
    prod = page.locator(".single-products").nth(0)
    prod.scroll_into_view_if_needed()
    prod.hover()
    prod.locator(".overlay-content .add-to-cart").click()
    page.get_by_role("button", name="Continue Shopping").click() 
    page.get_by_role("link", name="Cart").click()


""" Test Case 21: Add review on product
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Click on 'Products' button
        4. Verify user is navigated to ALL PRODUCTS page successfully
        5. Click on 'View Product' button
        6. Verify 'Write Your Review' is visible
        7. Enter name, email and review
        8. Click 'Submit' button
        9. Verify success message 'Thank you for your review.'
"""
def test21(page: Page):
    check(page)


""" Test Case 22: Add to cart from Recommended items
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Scroll to bottom of page
        4. Verify 'RECOMMENDED ITEMS' are visible
        5. Click on 'Add To Cart' on Recommended product
        6. Click on 'View Cart' button
        7. Verify that product is displayed in cart page
"""
def test22(page: Page):
    check(page)


""" Test Case 23: Verify address details in checkout page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click 'Signup / Login' button
        5. Fill all details in Signup and create account
        6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        7. Verify ' Logged in as username' at top
        8. Add products to cart
        9. Click 'Cart' button
        10. Verify that cart page is displayed
        11. Click Proceed To Checkout
        12. Verify that the delivery address is same address filled at the time registration of account
        13. Verify that the billing address is same address filled at the time registration of account
        14. Click 'Delete Account' button
        15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""
def test23(page: Page):
    check(page)


""" Test Case 24: Download Invoice after purchase order
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Add products to cart
        5. Click 'Cart' button
        6. Verify that cart page is displayed
        7. Click Proceed To Checkout
        8. Click 'Register / Login' button
        9. Fill all details in Signup and create account
        10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        11. Verify ' Logged in as username' at top
        12. Click 'Cart' button
        13. Click 'Proceed To Checkout' button
        14. Verify Address Details and Review Your Order
        15. Enter description in comment text area and click 'Place Order'
        16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
        17. Click 'Pay and Confirm Order' button
        18. Verify success message 'Your order has been placed successfully!'
        19. Click 'Download Invoice' button and verify invoice is downloaded successfully.
        20. Click 'Continue' button
        21. Click 'Delete Account' button
        22. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""
def test24(page: Page):
    check(page)


""" Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Scroll down page to bottom
        5. Verify 'SUBSCRIPTION' is visible
        6. Click on arrow at bottom right side to move upward
        7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
"""
def test25(page: Page):
    check(page)


""" Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Scroll down page to bottom
        5. Verify 'SUBSCRIPTION' is visible
        6. Scroll up page to top
        7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
"""
def test26(page: Page):
    check(page)

    

