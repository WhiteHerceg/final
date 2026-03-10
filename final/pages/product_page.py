from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def get_product_name(self):
        """Return the product title text shown on the page."""
        return self.browser.find_element(*ProductPageLocators.NAME).text

    def get_product_price(self):
        """Return the product price text shown on the page."""
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def add_to_basket_with_quiz(self):     
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click() 
        self.browser.implicitly_wait(5)
        self.solve_quiz_and_get_code()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.NAME_IN_MESSAGE))
        name = self.get_product_name()
        price = self.get_product_price()
        self.should_be_equal_product_name(name)
        self.should_be_equal_product_price(price)
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.NAME_IN_MESSAGE))
        name = self.get_product_name()
        price = self.get_product_price()
        self.should_be_equal_product_name(name)
        self.should_be_equal_product_price(price)
    

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_equal_product_name(self, expected_name):
        """Assert that the name shown in the success message equals the provided value."""
        product_name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        assert expected_name == product_name_in_message, (
            f"Product name in message is not equal to expected name: "
            f"expected '{expected_name}', got '{product_name_in_message}'"
        )

    def should_be_equal_product_price(self, expected_price):
        """Assert that the price shown in the success message equals the provided value."""
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert expected_price == product_price_in_message, (
            f"Product price in message is not equal to expected price: "
            f"expected '{expected_price}', got '{product_price_in_message}'"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_IN_MESSAGE), "Success message is presented, but should not be"

    def presence_of_element_located(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_IN_MESSAGE), "Success message is presented"

    def go_to_login_page(self):
       login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
       login_link.click()
    
    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"