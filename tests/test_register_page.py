import pytest
from pages.register_page import RegisterPage


@pytest.mark.skip
def test_go_to_register(browser):
    """ Now only one company needs to be created, so the test is skipped """
    link = 'https://web.teambooktest.com/register'
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_first_name()
    page.go_to_last_name()
    page.go_to_email()
    page.go_to_company_name()
    page.go_to_password()
    page.go_to_agreement_checkbox()
    page.go_to_create_organization_button()
