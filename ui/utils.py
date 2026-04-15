from playwright.sync_api import expect
from faker import Faker
import random

fake = Faker()

def generate_random_user():
    return { "name"          :   fake.name(),
             "email"         :   fake.email(), 
             "password"      :   fake.password(length=6),
             "number"        :   fake.phone_number(),
             "day"           :   random.randint(1, 31), 
             "month"         :   fake.month(),
             "year"          :   fake.year(),
             "card_number"   :   fake.credit_card_number(),
             "card_expire"   :   fake.credit_card_expire(),
             "card_cvv"      :   fake.credit_card_security_code()}


def check(page):
    page.goto("https://automationexercise.com")
    if "#google_vignette" in page.url:
        page.goto("https://automationexercise.com/test_cases")
    expect(page).to_have_title("Automation Exercise") 
    return   


def create_user(page):
    data = generate_random_user()
    page.get_by_placeholder("Name").fill(data["name"])
    page.locator("[data-qa='signup-email']").fill(data["email"])
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("ENTER ACCOUNT INFORMATION")).to_be_visible()
    page.get_by_label("Mr.").click() # hardcoded this btw
    page.get_by_label("Password").fill(data["password"])
    page.select_option('#days', str(data["day"]))
    page.select_option('#months', str(int(data["month"])))
    page.select_option('#years', data["year"])
    page.get_by_label("Sign up for our newsletter!").click()
    page.get_by_label("Receive special offers from our partners!").click()
    page.locator("#first_name").fill(data["name"])
    page.locator("#last_name").fill(data["name"])
    page.locator("#company").fill(data["name"])
    page.locator("#address1").fill(data["name"])
    page.locator("#address2").fill(data["name"])
    page.select_option('#country', 'United States')
    page.locator("#state").fill(data["name"])
    page.locator("#city").fill(data["name"])
    page.locator("#zipcode").fill(data["name"])
    page.locator("#mobile_number").fill(data["name"])
    page.get_by_role("button", name="Create Account").click()
    expect(page.get_by_role("heading", name="ACCOUNT CREATED!", exact=False)).to_be_visible() 
    page.get_by_role("link", name="Continue").click()
    expect(page.get_by_text(f"Logged in as {data['name']}")).to_be_visible()
    return data


def create_context(browser):
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://automationexercise.com/login")
    data_user = create_user(page1) 
    context1.close()
    context2 = browser.new_context()
    page = context2.new_page()
    
    return {"page"      : page,
            "data_user" : data_user}



def add_product_to_cart(page):
    collected = set()
    added_products = []
    for i in range(0, 2):
        idx = random.randint(0, 32)
        while idx in collected:
            idx = random.randint(0, 32)
        collected.add(idx)
        prod = page.locator(".single-products").nth(idx)

        product_name = prod.locator("p").first.inner_text()
        added_products.append(product_name)

        prod.scroll_into_view_if_needed()
        prod.hover()
        btn_add = prod.locator(".overlay-content .add-to-cart")
        btn_add.wait_for(state="visible") 
        btn_add.click()
        
        continue_btn = page.get_by_role("button", name="Continue Shopping")
        
        continue_btn.wait_for(state="visible", timeout=5000) 
        continue_btn.click()
        
        expect(page.locator("#cartModal")).to_be_hidden()
    return added_products