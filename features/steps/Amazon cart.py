from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input table on search field')
def search_product(context):
 context.driver.find_element(By. ID, 'twotabsearchtextbox'). SEND.KEYS('table');

@When('Click on the second product')
 def Click_second_product(context):
     context.driver.find_elements('By. Xpath, 's-image').click()

@When('Click on add to cart button')
def click_add_to_cart_button(By. CSS_SELECTOR, 'a-declarative').click()

@then('Verify cart has the item')
def item_on_the_cart(context);
    actual_result = context.driver.find_element('By ID, 'nav-cart-count)
    expected_result = "table"

     assert expected_result == actual_result, f'Expected{expected_result}, but got {actual_result}'

     context.driver.quit()