from pages.users_page import UsersPage
from pages.settings import url_users_page


def filter_users(browser):
    """ Function to filter users """
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.filter_users()