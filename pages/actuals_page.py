from .base_page import BasePage
from .locators import ActualsPageLocators
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .settings import ADMIN_VALID_EMAIL, ADMIN_VALID_PASSWORD


class ActualsPage(BasePage):
    def approve_logs_click(self):
        self.browser.find_element(*ActualsPageLocators.APPROVE_LOGS_BTN).click()

    def bulk_approve(self):
        self.browser.find_element(*ActualsPageLocators.BULK_APPROVE_BTN).click()
        self.browser.find_element(*ActualsPageLocators.SELECT_USERS_DROPDOWN).click()
        self.browser.find_element(*ActualsPageLocators.SELECT_USER).click()
        self.browser.find_element(*ActualsPageLocators.BULK_APPROVE_SUBMIT_BTN).click()

    def go_to_actual_page(self):
        actual_link = self.browser.find_element(*ActualsPageLocators.ACTUALS_LINK)
        actual_link.click()

    def date_select_actual_page(self):
        """Переход на страницу Actuals,
         создание заметки в календаре. """
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        val_time = '2'
        val_project = 'Example Project 2'
        val_note = 'double_click - our everything'
        self.browser.find_element(*ActualsPageLocators.LINK_PAGE_ACTUALS).click()
        select_day = self.browser.find_element(*ActualsPageLocators.CHOOSING_THE_DAY)
        btn_log_time_on_day = self.browser.find_element(*ActualsPageLocators.ADD_LOG_TIME)
        ActionChains(self.browser).move_to_element(select_day). \
            move_to_element(btn_log_time_on_day).double_click(btn_log_time_on_day).perform()
        """Заполнение формы"""
        line_time_new = self.browser.find_element(*ActualsPageLocators.TIME_FIELD_FORM_ADD_NOTE)
        line_project_new = self.browser.find_element(*ActualsPageLocators.PROJECT_FIELD_ADD_NOTE)
        ActionChains(self.browser).click(line_time_new).double_click(line_time_new). \
            send_keys(val_time).send_keys_to_element(line_project_new, val_project + Keys.ENTER).perform()
        self.browser.find_element(*ActualsPageLocators.NOTES_FIELD_ADD_NOTE).send_keys(val_note)
        self.browser.find_element(*ActualsPageLocators.BTN_ADD_NOTE).click()

    def checking_for_an_emerging_window(self):
        """Проверка и закрытие всплывающего окна на странице Actuals"""
        self.browser.maximize_window()
        self.browser.find_element(*ActualsPageLocators.LINK_PAGE_ACTUALS).click()
        try:
            self.browser.find_element(*ActualsPageLocators.POP_UP_WINDOW_BTN).click()
        except NoSuchElementException:
            print("There is no pop-up window")

    def fix_form_filling_actual_page(self):
        """Внесение исправлений в созданную заметку"""
        self.browser.maximize_window()
        fix_val_time = '3,6'
        fix_val_project = 'Example Project 1'
        self.browser.find_element(*ActualsPageLocators.LINK_PAGE_ACTUALS).click()
        event = self.browser.find_elements(*ActualsPageLocators.NOTES_IN_CALENDAR)
        try:
            if len(event) > 0:
                event[0].click()
            line_time = self.browser.find_element(*ActualsPageLocators.TIME_FIELD_FORM_ADD_NOTE)
            line_project = self.browser.find_element(*ActualsPageLocators.PROJECT_FIELD_ADD_NOTE)
            ActionChains(self.browser).click(line_time).double_click(line_time).send_keys(fix_val_time). \
                send_keys_to_element(line_project, fix_val_project + Keys.ENTER).perform()
            self.browser.find_element(*ActualsPageLocators.BTN_ADD_NOTE).click()
        except NoSuchElementException:
            print('There are no items in the calendar')
