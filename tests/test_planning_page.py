import time
from utils.login import login
from pages.planning_page import PlanningPage
from pages.settings import url_planning_page
import pytest


def test_go_to_next_month(browser):
    """ Move to the next month of the calendar """
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = PlanningPage(browser, link)
    page.open()
    page.go_to_next_page_calendar()
    time.sleep(3)


def test_go_to_previous_month(browser):
    """ Move to the previous month of the calendar """
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = PlanningPage(browser, link)
    page.open()
    page.go_to_previous_page_calendar()
    time.sleep(3)


def test_go_to_today_calendar_button(browser):
    """ Jump to calendar by button. """
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = PlanningPage(browser, link)
    page.open()
    page.go_to_calendar_button()
    time.sleep(3)


def test_add_user_button_create_user(browser):
    """ Test for create new user.
    BUG - there is a check on the uniqueness of the name and surname. But
        users can be of the same name. """
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = PlanningPage(browser, link)
    page.open()
    page.go_to_add_user_button()
    page.go_to_create_user_button()
    page.add_user_to_the_team()
    time.sleep(3)


@pytest.mark.skip
def test_go_to_search_name(browser):
    """ Search by name (Not find locator for search)"""
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = PlanningPage(browser, link)
    page.open()
    page.search_name()
    time.sleep(5)










