from selenium.webdriver.common.by import By
from pages.base_page import Page



class Main(Page):
    def open_main(self):
        self.open_url(url='https://www.amazon.com/')