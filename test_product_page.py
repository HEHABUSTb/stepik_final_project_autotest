import pytest
from .pages.product_page import ProductPage
import time

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

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket() #add product to basket
    time.sleep(1)
    product_page.solve_quiz_and_get_code() #solve puzzle


    product_page.should_be_correct_product_price_in_basket()  #Check price in basket
    product_page.should_be_correct_product_name_in_basket() #Check name of product in basket
    time.sleep(1)