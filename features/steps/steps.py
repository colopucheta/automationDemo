from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch the browser')
def open_browser(context):
    context.driver = webdriver.Chrome()


@when('I open the Web Application')
def navigate_to_web(context):
    context.driver.get("https://www.saucedemo.com/")


@when('enter valid credentials')
def enter_credentials(context):
    username = context.driver.find_element(By.ID("user-name"))
    username.


@then('the user is logged in')
def click_login(context):



@given('the user is in Inventory Page')
def navigate_to_inventory(context):


@when('the user adds an item to cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user adds an item to cart')


@then('verify that the cart counter increments')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the cart counter increments')


@given('the user has items added to cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has items added to cart')


@when('the user navigates to the Cart Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user navigates to the Cart Page')


@then('verify that the Cart Page contains the selected items')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the Cart Page contains the selected items')
