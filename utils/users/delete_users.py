from pages.users_page import UsersPage
from pages.settings import url_users_page


def delete_user(browser):
    """ Function to deactivate user """
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.delete_user()