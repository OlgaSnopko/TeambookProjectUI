import time

from utils.login import login
from pages.actuals_page import ActualsPage
from pages.login_page import LoginPage
from pages.settings import *
import pytest


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


@pytest.mark.smoke
def test_click_on_approve_logs(browser):
    """ Open time approval page """
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_page)
    page.open()
    page.checking_for_an_emerging_window()
    page.open_approve_logs()


@pytest.mark.smoke
def test_sort_users(browser):
    """Sort users by approval and alphabet"""
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.sort_users()


@pytest.mark.smoke
def test_user_worklog(browser):
    """Select user, which work log will be displayed"""
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.select_user_worklog()


@pytest.mark.smoke
def test_select_worklog_month(browser):
    """Change current month of user's worklog"""
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.select_worklog_month()


@pytest.mark.smoke
def test_select_date_from_picker(browser):
    """Change year and month of user's worklog in the date picker"""
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.select_date_from_picker()


@pytest.mark.xfail(reason='Bug: dropdown is not closed, when team is unchecked')
def test_unselect_team(browser):
    """Unselect team which report is shown right now"""
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.unselect_team()


@pytest.mark.xfail(reason='Bug: user is able to bulk approve logged time several times')
def test_bulk_approve(browser):
    """ Bulk approve logged in time """
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.bulk_approve()


@pytest.mark.smoke
def test_download_report(browser):
    """ Download user's work log"""
    login(browser)
    time.sleep(1)
    page = ActualsPage(browser, url_actuals_approval)
    page.open()
    page.download_report()
    time.sleep(1)
