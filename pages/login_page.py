from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        login = "login"
        assert login in current_url, \
            f"Current URL is not consider '{login}' in current_url: '{current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"

    def register_new_user(self):
        f = Faker()
        email = f.email()
        password = f.password(length=10)
        self.email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(email)
        self.password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD1).send_keys(password)
        self.check_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD2).send_keys(password)
        self.registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()
