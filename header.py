from pages.base_page import Page
from selenium.webdriver.common.by import By



class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART = (By.ID, 'nav-cart-count')
    ORDER_LINK = (By.ID, 'nav-orders')
    SIGN_IN = (By.CSS_SELECTOR,'h1.a-spacing-small')


    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def click_order(self):
        self.click(*self.ORDER_LINK)

    def find_element(self, *SIGN_IN):
            self.find_element(*SIGN_IN)

    def verify_url_contains_query(self, query):
        self.verify_text(query, *self.SIGN_IN)


