from base_page import Page
from selenium.webdriver.common.by import By



class Header(Page):
    SEARCH_FIELD = (By. ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def input_search(self):
        self.input_text('Table', *self.SEARCH_FIELd)

    def click_search(self):
        self.click(*self.SEARCH_ICON)



