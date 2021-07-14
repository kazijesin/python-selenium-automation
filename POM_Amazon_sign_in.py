from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given("Open Amazon page")
def open_amazon(context):
    context.app.main_page.open_main()


@when("Click Amazon Orders link")
def click_order(context):
    #orders_link = context. driver.find_element(By.ID, 'nav-orders')
    context.app.header.click_order()


@then("Verify page has {expected_text}")
def verify_search_worked_1(context, expected_text):
    context.app.search_result_page.verify_search_worked_1(expected_text)
