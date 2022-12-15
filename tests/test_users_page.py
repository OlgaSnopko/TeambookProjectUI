import time
import pytest
from utils.login import login
from utils.users.create_users import create_user
from utils.users.deactivate_user import deactivate_user
from utils.users.reactivate_user import reactivate_user
from utils.users.filter import filter_users
from utils.users.export_user import export_users
from utils.users.delete_users import delete_user
from pages.users_page import UsersPage
from pages.settings import url_users_page


def test_create_user(browser):
    ''' Test for create new user+filter user. BUG - there is a check on the uniqueness of the name and surname. But
    users can be of the same name '''
    login(browser)
    time.sleep(3)
    create_user(browser)
    time.sleep(3)
    filter_users(browser)
    time.sleep(3)

@pytest.mark.xfail
def test_deactivate_user(browser):
    '''Test for deactivation and reactivation user '''
    login(browser)
    time.sleep(3)
    deactivate_user(browser)
    time.sleep(3)
    reactivate_user(browser)
    time.sleep(3)

def test_deactivate_user_by_icon(browser):
    '''Test for deactivation and reactivation user by icon '''
    login(browser)
    time.sleep(3)
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.deactivate_user_by_icon()
    time.sleep(3)

def test_delete_user_by_icon(browser):
    '''Test for delete user by icon '''
    login(browser)
    time.sleep(3)
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.delete_user_by_icon()
    time.sleep(3)


def test_edit_user(browser):
    '''Test  for editing a user '''
    login(browser)
    time.sleep(3)
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.edit_user()
    time.sleep(3)

def test_sort_by_name(browser):
    '''Sort list by name'''
    login(browser)
    time.sleep(3)
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.sort_by_name()
    time.sleep(3)


def test_sort_by_role(browser):
    '''Sort list by role'''
    login(browser)
    time.sleep(3)
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.sort_by_role()
    time.sleep(3)



def test_export_users(browser):
    login(browser)
    time.sleep(3)
    export_users(browser)
    time.sleep(3)

