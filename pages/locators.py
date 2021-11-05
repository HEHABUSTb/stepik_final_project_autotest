from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.XPATH, "//p[contains(text(), 'empty')]")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FOR_REGISTRATION = (By.NAME, 'registration-email')
    PASSWORD_FOR_REGISTRATION = (By.NAME, 'registration-password1')
    CONFIRM_PASSWORD_FOR_REGISTRATION = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators():
    add_basket = (By.CSS_SELECTOR, '.btn-add-to-basket')
    price_product = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    price_in_basket = (By.CSS_SELECTOR, '.alert .alertinner p strong')
    product_name = (By.CSS_SELECTOR, '.product_main h1')
    product_name_in_basket = (By.CSS_SELECTOR, '.alert .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')