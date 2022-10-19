from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I launch the browser')
def open_browser(context):
    context.driver = webdriver.Chrome()


@when('I open the Web Application')
def navigate_to_web(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I enter username "{username}" and "{password}"')
def enter_credentials(context,username,password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)


@then('I log in')
def click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@given('I am in Inventory Page')
def verify_user_is_in_inventory(context):
    title = context.driver.find_element(By.ID, "inventory_container").is_displayed()
    assert title is True

@when('I add an item to cart')
def add_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()


@then('verify that the cart counter increments')
def verify_cart_counter_increment(context):
    counter = context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert counter.text == "1"
    return counter


@then('I navigate to the Cart Page')
def navigate_to_cart(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


@then('verify that the Cart Page contains the selected items')
def step_impl(context):
    quantity = context.driver.find_element(By.CLASS_NAME, "cart_quantity")
    item_name = context.driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert quantity.text == "1"
    assert item_name.text == "Sauce Labs Backpack"
