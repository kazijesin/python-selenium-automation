from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_RESULT = (By.XPATH, "//a[@class='a-link-normal a-text-normal']")
    SEARCH_RESULT1 = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
    PRODUCT_RESULT1 = (By.CSS_SELECTOR, 'span.a-size-base-plus a-color-base a-text-normal')
    SEARCH_RESULT2 = SIGN_IN = (By.CSS_SELECTOR,'h1.a-spacing-small')




    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)

    def verify_search_worked(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)


    def verify_search_worked_1(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT2)





