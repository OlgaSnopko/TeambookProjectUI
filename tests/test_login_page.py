from pages.login_page import LoginPage
from pages.settings import url_login_page


def test_go_to_login(browser):
    """ Login process """
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.go_to_login_button()


def test_go_to_create_new_organization(browser):
    """ Go to the page to create a new organization """
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_create()


def test_go_to_forgot_password(browser):
    """ Go to the page if you forgot password """
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_forgot_password()
