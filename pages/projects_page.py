from .base_page import BasePage
from .locators import ProjectsPageLocators
from utils.clear_field import clear_field


class ProjectsPage(BasePage):
    def click_create_project_button(self):
        create_project_button = self.browser.find_element(*ProjectsPageLocators.CREATE_PROJECT_BTN)
        create_project_button.click()
    
    def fill_project_name(self, project_name):
        project_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME)
        project_name_field.send_keys(project_name)
    
    def fill_project_short_name(self, project_short_name):
        project_short_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME)
        project_short_name_field.send_keys(project_short_name)
    
    def click_client_field(self):
        client_field = self.browser.find_element(*ProjectsPageLocators.CLIENT)
        client_field.click()
    
    def select_client(self):
        select_client = self.browser.find_element(*ProjectsPageLocators.SELECT_CLIENT)
        select_client.click()
        
    def fill_estimated_hours(self):
        estimated_hours = self.browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS)
        estimated_hours.send_keys('32')
    
    def click_manager_field(self):
        manager_field = self.browser.find_element(*ProjectsPageLocators.MANAGER)
        manager_field.click()
    
    def select_manager(self):
        select_manager = self.browser.find_element(*ProjectsPageLocators.SELECT_MANAGER)
        select_manager.click()
    
    def select_status(self):
        status = self.browser.find_element(*ProjectsPageLocators.STATUS)
        status.click()
        option = self.browser.find_element(*ProjectsPageLocators.SELECT_STATUS)
        option.click()
    
    def fill_business_unit(self):
        business_unit = self.browser.find_element(*ProjectsPageLocators.BUSINESS_UNIT)
        business_unit.send_keys('test business unit')
    
    def click_define_start_end_dates_checkbox(self):
        define_start_end_dates_checkbox = self.browser.find_element(*ProjectsPageLocators.
                                                                    DEFINE_START_END_DATES_CHECKBOX)
        define_start_end_dates_checkbox.click()
    
    def click_project_color(self):
        project_color = self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR)
        project_color.click()
    
    def select_project_color(self):
        select_project_color = self.browser.find_element(*ProjectsPageLocators.SELECT_PROJECT_COLOR)
        select_project_color.click()
    
    def click_create_button(self):
        create_project_button = self.browser.find_element(*ProjectsPageLocators.CREATE_BTN)
        create_project_button.click()
    
    def fill_project_search_field(self, project_name):
        project_search_field = self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD)
        project_search_field.send_keys(project_name)
    
    def select_project_name(self):
        select_project_name = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME_SELECT)
        select_project_name.click()
    
    def click_archive_project_icon(self):
        archive_project_icon = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_ICON)
        archive_project_icon.click()
        
    def click_archive_project_button(self):
        archive_project_button = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN)
        archive_project_button.click()
    
    def filter_project_by_activity(self):
        filter_project_by_activity = self.browser.find_element(*ProjectsPageLocators.FILTER_PROJECTS_BY_ACTIVITY)
        filter_project_by_activity.click()
    
    def select_archive_projects(self):
        select_archive_projects = self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVE_PROJECTS)
        select_archive_projects.click()
    
    def click_archive_project_checkbox(self):
        archive_project_checkbox = self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVE_PROJECT_CHECKBOX)
        archive_project_checkbox.click()
    
    def click_delete_archive_project_icon(self):
        delete_archive_project_icon = self.browser.find_element(*ProjectsPageLocators.DELETE_ARCHIVE_PROJECT_ICON)
        delete_archive_project_icon.click()
    
    def click_delete_project_button(self):
        delete_project_button = self.browser.find_element(*ProjectsPageLocators.DELETE_PROJECT_BTN)
        delete_project_button.click()

    def click_manage_clients_button(self):
        manage_clients_button = self.browser.find_element(*ProjectsPageLocators.MANAGE_CLIENTS_BTN)
        manage_clients_button.click()

    def click_create_client_button(self):
        create_client_button = self.browser.find_element(*ProjectsPageLocators.CREATE_CLIENT_BTN)
        create_client_button.click()

    def fill_client_name(self):
        fill_client_name = self.browser.find_element(*ProjectsPageLocators.CLIENT_NAME)
        fill_client_name.send_keys('test client')

    def fill_client_email(self):
        fill_client_email = self.browser.find_element(*ProjectsPageLocators.CLIENT_EMAIL)
        fill_client_email.send_keys('testemail@gmail.com')

    def fill_client_phone(self):
        fill_client_phone = self.browser.find_element(*ProjectsPageLocators.CLIENT_PHONE)
        fill_client_phone.send_keys('89623455445')

    def click_save_client_button(self):
        save_client_button = self.browser.find_element(*ProjectsPageLocators.SAVE_CLIENT_BTN)
        save_client_button.click()

    def fill_client_search_field(self):
        fill_client_search_field = self.browser.find_element(*ProjectsPageLocators.SEARCH_CLIENT_FIELD)
        fill_client_search_field.send_keys('test client')

    def click_edit_client_button(self):
        edit_client_button = self.browser.find_element(*ProjectsPageLocators.EDIT_CLIENT_BTN)
        edit_client_button.click()

    def edit_client_name(self):
        edit_client_name = self.browser.find_element(*ProjectsPageLocators.EDIT_CLIENT_NAME)
        clear_field(edit_client_name)
        edit_client_name.send_keys('test client1')

    def edit_client_email(self):
        edit_client_email = self.browser.find_element(*ProjectsPageLocators.EDIT_CLIENT_EMAIL)
        clear_field(edit_client_email)
        edit_client_email.send_keys('testemail1@gmail.com')

    def edit_client_phone(self):
        edit_client_phone = self.browser.find_element(*ProjectsPageLocators.EDIT_CLIENT_PHONE)
        clear_field(edit_client_phone)
        edit_client_phone.send_keys('89623455441')

    def click_save_edit_client_button(self):
        save_edit_client_button = self.browser.find_element(*ProjectsPageLocators.SAVE_EDIT_CLIENT_BTN)
        save_edit_client_button.click()

    def click_delete_client_icon(self):
        delete_client_icon = self.browser.find_element(*ProjectsPageLocators.DELETE_CLIENT_ICON)
        delete_client_icon.click()

    def click_delete_client_button(self):
        delete_client_button = self.browser.find_element(*ProjectsPageLocators.DELETE_CLIENT_BTN)
        delete_client_button.click()
        