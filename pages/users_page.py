import time

from .base_page import BasePage
from .locators import UsersPageLocators
import uuid

name = (str(uuid.uuid4().hex))

class UsersPage(BasePage):
    def create_user(self):
        email=uuid.uuid4().hex
        create_users_button = self.browser.find_element(*UsersPageLocators.CREATE_NEW_USER_BUTTON)
        create_users_button.click()
        first_name_button = self.browser.find_element(*UsersPageLocators.FIRST_NAME_BUTTON)
        first_name_button.click()
        first_name_button.send_keys(f'{name}')
        last_name_button = self.browser.find_element(*UsersPageLocators.LAST_NAME_BUTTON)
        last_name_button.click()
        last_name_button.send_keys('NEVSKAYA')
        email_button = self.browser.find_element(*UsersPageLocators.EMAIL_BUTTON)
        email_button.click()
        email_button.send_keys(f'{email}@uy.lk')
        teams_button = self.browser.find_element(*UsersPageLocators.TEAMS_BUTTON)
        teams_button.click()
        choose_company = self.browser.find_element(*UsersPageLocators.CHOOSE_COMPANY)
        choose_company.click()
        phone_number = self.browser.find_element(*UsersPageLocators.PHONE_NUMBER)
        phone_number.click()
        phone_number.send_keys('728648723')
        create_button = self.browser.find_element(*UsersPageLocators.CREATE_BUTTON)
        create_button.click()





    def edit_user(self):
        open_edit_form = self.browser.find_element(*UsersPageLocators.OPEN_EDIT_FORM1)
        open_edit_form.click()
        edit_user_button = self.browser.find_element(*UsersPageLocators.EDIT_USER_BUTTON)
        edit_user_button.click()
        change_user_role_button = self.browser.find_element(*UsersPageLocators.USER_ROLE_BUTTON)
        change_user_role_button.click()
        choose_user_role = self.browser.find_element(*UsersPageLocators.CHOOSE_USER_ROLE)
        choose_user_role.click()
        save_edit_button = self.browser.find_element(*UsersPageLocators.SAVE_BUTTON)
        save_edit_button.click()





    def deactivate_user(self):
        open_edit_form = self.browser.find_element(*UsersPageLocators.OPEN_EDIT_FORM)
        open_edit_form.click()
        delete_button = self.browser.find_element(*UsersPageLocators.DELETE_BUTTON)
        delete_button.click()
        deactivate_button = self.browser.find_element(*UsersPageLocators.DEACTIVATE_BUTTON)
        deactivate_button.click()

    def deactivate_user_by_icon(self):
        select_user_check_box= self.browser.find_element(*UsersPageLocators.SELECT_USER_CHECK_BOX)
        select_user_check_box.click()
        deactivate_icon = self.browser.find_element(*UsersPageLocators.DEACTIVATE_ICON)
        deactivate_icon.click()
        deactivate_button_on_form = self.browser.find_element(*UsersPageLocators.DEACTIVATE_BUTTON)
        deactivate_button_on_form.click()
        active_button = self.browser.find_element(*UsersPageLocators.ACTIVE_BUTTON)
        active_button.click()
        deactivate_dropdown = self.browser.find_element(*UsersPageLocators.DEACTIVATE_DROPDOWN)
        deactivate_dropdown.click()
        select_user_for_activate = self.browser.find_element(*UsersPageLocators.SELECT_USER_FOR_ACTIVATE)
        select_user_for_activate.click()
        time.sleep(3)
        reactivate_icon = self.browser.find_element(*UsersPageLocators.RACTIVATE_ICON)
        reactivate_icon.click()
        time.sleep(3)
        reactivate_button_on_form=self.browser.find_element(*UsersPageLocators.REACTIVATE_BUTTON)
        reactivate_button_on_form.click()
        time.sleep(3)

    def delete_user_by_icon(self):
        select_user_check_box = self.browser.find_element(*UsersPageLocators.SELECT_USER_CHECK_BOX)
        select_user_check_box.click()
        deactivate_icon = self.browser.find_element(*UsersPageLocators.DEACTIVATE_ICON)
        deactivate_icon.click()
        deactivate_button_on_form = self.browser.find_element(*UsersPageLocators.DEACTIVATE_BUTTON)
        deactivate_button_on_form.click()
        active_button = self.browser.find_element(*UsersPageLocators.ACTIVE_BUTTON)
        active_button.click()
        deactivate_dropdown = self.browser.find_element(*UsersPageLocators.DEACTIVATE_DROPDOWN)
        deactivate_dropdown.click()
        select_user_for_activate = self.browser.find_element(*UsersPageLocators.SELECT_USER_FOR_ACTIVATE)
        select_user_for_activate.click()
        time.sleep(3)
        delete_icon = self.browser.find_element(*UsersPageLocators.DELETE_ICON)
        delete_icon.click()
        time.sleep(3)
        delete_button_on_form = self.browser.find_element(*UsersPageLocators.DELETE_BUTTON_IN_DELETE_FORM)
        delete_button_on_form.click()
        time.sleep(3)


    def reactivate_user(self):
        active_button = self.browser.find_element(*UsersPageLocators.ACTIVE_BUTTON)
        active_button.click()
        deactivate_dropdown = self.browser.find_element(*UsersPageLocators.DEACTIVATE_DROPDOWN)
        deactivate_dropdown.click()
        select_user_for_activate = self.browser.find_element(*UsersPageLocators.SELECT_USER_FOR_ACTIVATE)
        select_user_for_activate.click()
        reactivate_icon = self.browser.find_element(*UsersPageLocators.RACTIVATE_ICON)
        reactivate_icon.click()
        reactivate_button= self.browser.find_element(*UsersPageLocators.REACTIVATE_BUTTON)
        reactivate_button.click()

    def export_users(self):
        check_box_user = self.browser.find_element(*UsersPageLocators.CHECK_BOX_USER)
        check_box_user.click()
        export_users_button=self.browser.find_element(*UsersPageLocators.EXPORT_BUTTON)
        export_users_button.click()

    def sort_by_name(self):
        sort_by_name_button=self.browser.find_element(*UsersPageLocators.SORT_BY_NAME_BUTTON)
        sort_by_name_button.click()

    def sort_by_role(self):
        sort_by_role_button = self.browser.find_element(*UsersPageLocators.SORT_BY_ROLE)
        sort_by_role_button.click()



    def filter_users(self):
        filter_input = self.browser.find_element(*UsersPageLocators.FILTER_INPUT)
        filter_input.click()
        filter_input.send_keys(f'{name}')

    def delete_user(self):
        active_button = self.browser.find_element(*UsersPageLocators.ACTIVE_BUTTON)
        active_button.click()
        deactivate_dropdown = self.browser.find_element(*UsersPageLocators.DEACTIVATE_DROPDOWN)
        deactivate_dropdown.click()
        filter_input = self.browser.find_element(*UsersPageLocators.FILTER_INPUT)
        filter_input.click()
        filter_input.send_keys(f'{name}')
        time.sleep(3)
        select_user_check_box = self.browser.find_element(*UsersPageLocators.SELECT_USER_FOR_ACTIVATE)
        select_user_check_box.click()
        time.sleep(3)
        delete_icon = self.browser.find_element(*UsersPageLocators.DELETE_ICON)
        delete_icon.click()
        time.sleep(3)
        delete_button_in_delete_form=self.browser(*UsersPageLocators.DELETE_BUTTON_IN_DELETE_FORM)
        delete_button_in_delete_form.click()



