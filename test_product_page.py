import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from random_word import RandomWords
import time

"""
links =  ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

links[7] = pytest.param(links[7], marks=pytest.mark.xfail)
"""

@pytest.mark.user_check
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.random_words = RandomWords()
        self.email = self.random_words.get_random_word() + "@fakesmail.org"
        self.password = self.random_words.get_random_word() + '123s'
        self.page.register_new_user(self.email, self.password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()  # check we don't have success message
        product_page.add_product_to_basket()  # add product to basket
        product_page.solve_quiz_and_get_code()  # solve puzzle
        product_page.success_message_should_disappear()  # check what success message disappear
        product_page.should_be_correct_product_price_in_basket()  # Check price in basket
        product_page.should_be_correct_product_name_in_basket()  # Check name of product in basket

#@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message() #check we don't have success message
    product_page.add_product_to_basket() #add product to basket

    product_page.solve_quiz_and_get_code() #solve puzzle
    product_page.success_message_should_disappear() #check what success message disappear

    product_page.should_be_correct_product_price_in_basket()  #Check price in basket
    product_page.should_be_correct_product_name_in_basket() #Check name of product in basket

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_should_be_empty()
    page.empty_basket_should_contain_text()
