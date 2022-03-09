from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from .locators import ProductPageLocators

class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME), \
                "Product name is presented, but should not be"

    def is_basket_message_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), (
            "Message about adding is not presented")
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in message, "No product name in the message"