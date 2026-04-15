from playwright.sync_api import expect
from faker import Faker

fake = Faker()

def generate_random_user():
    return { "name"          :   fake.name(),
             "email"         :   fake.email(), 
             "password"      :   fake.password(length=6),
             "number"        :   fake.phone_number(),
             "day"           :   fake.day_of_month(), 
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
    page.locator(".signup-form [data-qa='signup-email']").fill(data["email"])
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

def add_product_to_cart(page):
    return