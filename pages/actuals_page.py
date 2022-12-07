from .base_page import BasePage
from .locators import ActualsPageLocators
from .settings import ADMIN_VALID_EMAIL, ADMIN_VALID_PASSWORD


class ActualsPage(BasePage):
    def approve_logs_click(self):
        self.browser.find_element(*ActualsPageLocators.APPROVE_LOGS_BTN).click()

    def bulk_approve(self):
        self.browser.find_element(*ActualsPageLocators.BULK_APPROVE_BTN).click()
        self.browser.find_element(*ActualsPageLocators.SELECT_USERS_DROPDOWN).click()
        self.browser.find_element(*ActualsPageLocators.SELECT_USER).click()
        self.browser.find_element(*ActualsPageLocators.BULK_APPROVE_SUBMIT_BTN).click()