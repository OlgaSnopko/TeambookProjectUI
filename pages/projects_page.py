from .base_page import BasePage
from .locators import ProjectsPageLocators


class ProjectsPage(BasePage):
    def go_to_create_project_button(self):
        create_project_button = self.browser.find_element(*ProjectsPageLocators.CREATE_PROJECT_BTN)
        create_project_button.click()
    
    def go_to_project_name(self, project_name):
        project_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME)
        project_name_field.send_keys(project_name)
    
    def go_to_project_short_name(self, project_short_name):
        project_short_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME)
        project_short_name_field.send_keys(project_short_name)
    
    def go_to_client(self):
        client = self.browser.find_element(*ProjectsPageLocators.CLIENT)
        client.click()
    
    def go_to_select_client(self):
        select_client = self.browser.find_element(*ProjectsPageLocators.SELECT_CLIENT)
        select_client.click()
        
    def go_to_estimated_hours(self):
        estimated_hours = self.browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS)
        estimated_hours.send_keys('32')
    
    def go_to_manager(self):
        manager = self.browser.find_element(*ProjectsPageLocators.MANAGER)
        manager.click()
    
    def go_to_select_manager(self):
        select_manager = self.browser.find_element(*ProjectsPageLocators.SELECT_MANAGER)
        select_manager.click()
    
    def go_to_status(self):
        status = self.browser.find_element(*ProjectsPageLocators.STATUS)
        status.click()
        option = self.browser.find_element(*ProjectsPageLocators.SELECT_STATUS)
        option.click()
    
    def go_to_select_status(self):
        select_status = self.browser.find_element(*ProjectsPageLocators.SELECT_STATUS)
        select_status.send_keys('Done')
    
    def go_to_business_unit(self):
        business_unit = self.browser.find_element(*ProjectsPageLocators.BUSINESS_UNIT)
        business_unit.send_keys('test business unit')
    
    def go_to_define_start_end_dates_checkbox(self):
        define_start_end_dates_checkbox = self.browser.find_element(*ProjectsPageLocators.DEFINE_START_END_DATES_CHECKBOX)
        define_start_end_dates_checkbox.click()
    
    def go_to_project_color(self):
        project_color = self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR)
        project_color.click()
    
    def go_to_select_project_color(self):
        select_project_color = self.browser.find_element(*ProjectsPageLocators.SELECT_PROJECT_COLOR)
        select_project_color.click()
    
    def go_to_create_button(self):
        create_button = self.browser.find_element(*ProjectsPageLocators.CREATE_BTN)
        create_button.click()
    
    def go_to_search_field(self, project_name):
        search_field = self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD)
        search_field.send_keys(project_name)
    
    def go_to_project_name_select(self):
        project_name_select = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME_SELECT)
        project_name_select.click()
    
    def go_to_archive_project_icon(self):
        archive_project_icon = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_ICON)
        archive_project_icon.click()
        
    def go_to_archive_project_button(self):
        archive_project_button = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN)
        archive_project_button.click()
    
    def go_to_filter_project_by_activity(self):
        filter_project_by_activity = self.browser.find_element(*ProjectsPageLocators.FILTER_PROJECTS_BY_ACTIVITY)
        filter_project_by_activity.click()
    
    def go_to_select_archive_projects(self):
        select_archive_projects = self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVE_PROJECTS)
        select_archive_projects.click()
    
    def go_to_select_archive_project_checkbox(self):
        select_archive_project_checkbox = self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVE_PROJECT_CHECKBOX)
        select_archive_project_checkbox.click()
    
    def go_to_delete_archive_project_icon(self):
        delete_archive_project_icon = self.browser.find_element(*ProjectsPageLocators.DELETE_ARCHIVE_PROJECT_ICON)
        delete_archive_project_icon.click()
    
    def go_to_delete_project_button(self):
        delete_archive_project_button = self.browser.find_element(*ProjectsPageLocators.DELETE_PROJECT_BTN)
        delete_archive_project_button.click()