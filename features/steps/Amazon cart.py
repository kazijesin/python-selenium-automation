from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver


@given('Open Amazon page1')
def open_amazon(context):
    context.driver = webdriver.Chrome(executable_path='/Users/raihanamin/Automation/python-selenium-automation/chromedriver')
    context.driver.get('https://www.amazon.com/')


@when('Input Table in search field')
def search_product(context):
 context.driver.find_elements(By.ID, 'twotabsearchtextbox').send_keys('Table')

@when('Click on Amazon search icon')
def click_search(context):
     context.driver.find_elements(By.ID, 'nav-search-submit-button').click()

@when('Click on first product')
def click_first_product(context):
     context.driver.find_elements(By.XPATH, 's-image').click()

@when('Click add to cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a-declarative').click()

@then('Verify cart has one item')
def item_on_the_cart(context):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count')
    expected_result = "one item"
    assert expected_result == actual_result, f'Expected{expected_result}, but got {actual_result}'
    context.driver.quit()