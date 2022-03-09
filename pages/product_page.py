from .base_page import BasePage
from .basket_page import BasketPage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators



class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.ADD_MESSAGE), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUM_MESSAGE), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(*ProductPageLocators.BASKET_SUM_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

    def can_go_to_login_page_from_product_page():
        pass
        