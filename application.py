from pages.header import Header
from pages.main_page import Main
from pages.product_page import ProductPage
from pages.search_result_page import SearchResults



class Application:

    def __init__(self,driver):
     self.driver = driver

     self.main_page = Main(self.driver)
     self.header = Header(self.driver)
     self.product_page = ProductPage(self.driver)
     self.search_result_page = SearchResults(self.driver)

