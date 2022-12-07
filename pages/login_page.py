from .base_page import BasePage
from .locators import LoginPageLocators
from .settings import ADMIN_VALID_EMAIL, ADMIN_VALID_PASSWORD


class LoginPage(BasePage):
    def go_to_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(ADMIN_VALID_EMAIL)

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(ADMIN_VALID_PASSWORD)

    def go_to_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def go_to_create(self):
        organization_create = self.browser.find_element(*LoginPageLocators.CREATE_BUTTON)
        organization_create.click()

    def go_to_forgot_password(self):
        forgot_password = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        forgot_password.click()
