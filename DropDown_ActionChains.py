from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given("Open Amazon product page")
def amazon_product_page(context):
    context.app.main_page.open_product_page()

@when("Hover over new arrivals")
def hover_over_new_arrivals(context):
    context.app.header.hover_over_new_arrivals()

@when("Select Garden & Outdoor department")
def select_department(context):
        context.app.header.select_department()

@then("Verify Garden & Outdoor department is selected")
def verify_garden_department(context):
    context.app.search_result_page.verify_garden_department()



