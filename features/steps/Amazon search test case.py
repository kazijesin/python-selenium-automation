from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display")

@then('PHelp search for {cancel_order} are shown')
def verify_found_results_text(context, cancel_order):
    assert 'cancel_order' in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
