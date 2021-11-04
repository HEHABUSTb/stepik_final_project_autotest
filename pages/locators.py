from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    add_basket = (By.CSS_SELECTOR, '.btn-add-to-basket')
    price_product = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    price_in_basket = (By.CSS_SELECTOR, '.alert .alertinner p strong')
    product_name = (By.CSS_SELECTOR, '.product_main h1')
    product_name_in_basket = (By.CSS_SELECTOR, '.alert .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'success_message')