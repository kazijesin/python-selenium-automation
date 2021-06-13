from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@when('Click {best seller}')
def best_seller(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.nav-a").click()


@then('Verify page display five links')
def page_display(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'li.zg_selected')
    expected_result = "five links"
    assert expected_result == actual_result, f'Expected {expected_result}, but got{actual_result}'

    context.driver.quit()
