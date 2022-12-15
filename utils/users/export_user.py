from pages.users_page import UsersPage
from pages.settings import url_users_page


def export_users(browser):
    """ Function to export selected users """
    link = url_users_page
    page = UsersPage(browser, link)
    page.open()
    page.export_users()