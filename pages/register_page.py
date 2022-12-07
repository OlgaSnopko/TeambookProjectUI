from .base_page import BasePage
from .locators import RegisterPageLocators
from .settings import ADMIN_VALID_EMAIL, ADMIN_VALID_PASSWORD


class RegisterPage(BasePage):
    def go_to_first_name(self):
        first_name = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        first_name.send_keys('teambook')

    def go_to_last_name(self):
        last_name = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        last_name.send_keys('test')

    def go_to_email(self):
        email = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email.send_keys(ADMIN_VALID_EMAIL)

    def go_to_company_name(self):
        company_name = self.browser.find_element(*RegisterPageLocators.COMPANY_NAME)
        company_name.send_keys('test company')

    def go_to_password(self):
        password = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        password.send_keys(ADMIN_VALID_PASSWORD)

    def go_to_agreement_checkbox(self):
        agreement_checkbox = self.browser.find_element(*RegisterPageLocators.AGREEMENT_CHECKBOX)
        agreement_checkbox.click()

    def go_to_create_organization_button(self):
        create_organization_button = self.browser.find_element(*RegisterPageLocators.CREATE_ORGANIZATION_BTN)
        create_organization_button.click()
