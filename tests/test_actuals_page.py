from pages.actuals_page import ActualsPage


def test_click_on_approve_logs(browser):
    """ temporary"""
    link = 'https://web.teambooktest.com/actuals'
    page = ActualsPage(browser, link)
    page.open()
    page.approve_logs_click()


def test_bulk_approve(browser):
    """ temporary"""
    link = 'https://web.teambooktest.com/actuals/approval'
    page = ActualsPage(browser, link)
    page.open()
    page.approve_logs_click()
