from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon bestsellers')
def open_amazon(context):
   context.driver.get('https://www.amazon.com/gp/bestsellers/')


@then('Verify there are {expected_links} links')
def verify_links_count (context, expected_links):
  actual_links = context.find_elements(By.CSS_SELECTOR, '#zg_tabs a')
  assert len(actual_links) == int(expected_links), f'Expected{expected_links}, but got {len(actual_links)}'

  context.driver.quit()


@given("Open the Amazon bestsellers page")
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path='/Users/raihanamin/Automation/python-selenium-automation/chromedriver')
    context.driver.get('https://www.amazon.com/gp/bestsellers/')


@then("Verify that there are 5 links")
def step_impl(context):
    actual_links = context.find_elements(By.CSS_SELECTOR, '#zg_tabs a')
    expected_links = 5
    assert len(actual_links) == int(expected_links), f'Expected{expected_links}, but got {len(actual_links)}'

    context.driver.quit()
