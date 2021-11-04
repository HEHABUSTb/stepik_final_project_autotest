from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.add_basket)
        add_to_basket.click()

    def should_be_correct_product_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.price_product).text
        basket_price = self.browser.find_element(*ProductPageLocators.price_in_basket).text
        #print('price = ', price, 'type of price =', type(price))
        #print('price = ', basket_total, 'type of price =', type(basket_total))
        assert price == basket_price, 'Price in basket not equal price of product'

    def should_be_correct_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.product_name_in_basket).text
        #print('Name = ', product_name, 'type of product name =', type(product_name))
        #print('Name = ', product_name_in_basket, 'type of in basket =', type(product_name_in_basket))
        #print(product_name == product_name_in_basket)
        assert  product_name == product_name_in_basket, 'Product name and name in basket is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

