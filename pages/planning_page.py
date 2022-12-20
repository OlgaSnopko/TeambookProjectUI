from .base_page import BasePage
from .locators import PlanningPageLocators
import uuid
name = (str(uuid.uuid4().hex))


class PlanningPage(BasePage):
    def go_to_next_page_calendar(self):
        forward_arrow = self.browser.find_element(*PlanningPageLocators.FORWARD_ARROW)
        forward_arrow.click()

    def go_to_previous_page_calendar(self):
        back_arrow = self.browser.find_element(*PlanningPageLocators.BACK_ARROW)
        back_arrow.click()

    def go_to_calendar_button(self):
        calendar_button = self.browser.find_element(*PlanningPageLocators.CALENDAR_BUTTON)
        calendar_button.click()

    def go_to_add_user_button(self):
        add_user_button = self.browser.find_element(*PlanningPageLocators.ADD_USER_BUTTON)
        add_user_button.click()

    def go_to_create_user_button(self):
        create_user_button = self.browser.find_element(*PlanningPageLocators.CREATE_USER_BUTTON)
        create_user_button.click()

    def add_user_to_the_team(self):
        email = uuid.uuid4().hex
        first_name = self.browser.find_element(*PlanningPageLocators.FIRST_NAME)
        first_name.click()
        first_name.send_keys(f'{name}')
        last_name = self.browser.find_element(*PlanningPageLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys('NORREY')
        email_name = self.browser.find_element(*PlanningPageLocators.EMAIL_NAME)
        email_name.click()
        email_name.send_keys(f'{email}@tb.tb')
        phone_number = self.browser.find_element(*PlanningPageLocators.PHONE_NUMBER)
        phone_number.click()
        phone_number.send_keys('2234567')
        user_role = self.browser.find_element(*PlanningPageLocators.USER_ROLE)
        user_role.click()
        user_role_add = self.browser.find_element(*PlanningPageLocators.USER_ROLE_ADD)
        user_role_add.click()
        submit_button = self.browser.find_element(*PlanningPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def search_name(self):
        search_name_user = self.browser.find_element(*PlanningPageLocators.SEARCH_NAME)
        search_name_user.click()
        search_name_user.send_keys('Anna')
        add_user_anna = self.browser.find_element(*PlanningPageLocators.ANNA)
        add_user_anna.click()












