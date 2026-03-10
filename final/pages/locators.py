from selenium.webdriver.common.by import By

class CartPageLocators():
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    
class BasePageLocators():
    CART_LINK = (By.XPATH, '//a[text()="View basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[text()='Add to basket']")

    NAME = (By.CSS_SELECTOR, ".product_main h1")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
