from pages.login_page import LoginPage
from pages.settings import url_login_page


def login(browser):
    """ Function to log in """
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.go_to_login_button()
    