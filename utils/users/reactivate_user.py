from pages.users_page import UsersPage
from pages.settings import url_users_page


def reactivate_user(browser):
    """ Function to reactivate user """
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.reactivate_user()