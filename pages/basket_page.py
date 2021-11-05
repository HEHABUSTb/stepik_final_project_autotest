from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Basket should be empty"

    def empty_basket_should_contain_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            'Should containt text about empty basket'
