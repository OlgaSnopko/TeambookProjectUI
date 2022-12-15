from pages.users_page import UsersPage
from pages.settings import url_users_page


def create_user(browser):
    """ Function to create user"""
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.create_user()