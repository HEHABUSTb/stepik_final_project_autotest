from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)

    product_page.open()
    product_page.add_product_to_basket() #add product to basket
    time.sleep(1)

    product_page.solve_quiz_and_get_code() #solve puzzle
    product_page.should_be_correct_product_price_in_basket()  #Check price in basket
    product_page.should_be_correct_product_name_in_basket() #Check name of product in basket
    time.sleep(1)