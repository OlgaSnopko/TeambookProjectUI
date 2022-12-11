from pages.actuals_page import ActualsPage
from pages.login_page import LoginPage
from pages.settings import *
import pytest


def test_click_on_approve_logs(browser):
    """ temporary"""
    link = 'https://web.teambooktest.com/actuals'
    page = ActualsPage(browser, link)
    page.open()
    page.approve_logs_click()


def test_bulk_approve(browser):
    """ temporary"""
    link = 'https://web.teambooktest.com/actuals/approval'
    page = ActualsPage(browser, link)
    page.open()
    page.approve_logs_click()


@pytest.mark.regression
def test_add_new_note(browser):
    """Add new note in the tab Actuals"""
    page = LoginPage(browser, url_login_page)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.go_to_login_button()
    page = ActualsPage(browser, url_actuals_page)
    page.checking_for_an_emerging_window()
    page.date_select_actual_page()


@pytest.mark.xfail(reason='Баг. Значение Duration (Hours) введенное вручную в календаре не округляется по 0,5.')
@pytest.mark.regression
def test_correction_note(browser):
    """Fix the created note"""
    page = LoginPage(browser, url_login_page)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.go_to_login_button()
    page = ActualsPage(browser, url_actuals_page)
    page.checking_for_an_emerging_window()
    page.fix_form_filling_actual_page()
