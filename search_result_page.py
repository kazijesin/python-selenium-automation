from base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_worked(self):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        expected_result = 'Table'
        assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

