import time
from utils.login import login
from utils.projects_page.clients import create_new_client, delete_client
from utils.projects_page.projects import get_projects_page, create_project, archive_project, delete_project


def test_create_project(browser):
    """ Create a new project from Projects tab """
    project_name = 'Test project'
    project_short_name = 'Test'
    login(browser)
    time.sleep(1)
    create_project(browser, project_name, project_short_name)


def test_archive_and_delete_project(browser):
    """ Archive and delete the project. Joint test because of impossibility to delete the project without archiving it
 """
    project_name = 'Test project 2'
    project_short_name = 'Test 2'
    login(browser)
    time.sleep(1)
    create_project(browser, project_name, project_short_name)
    archive_project(browser, project_name)
    delete_project(browser, project_name)
    
    
def test_create_new_client(browser):
    """ Create a new client from Projects tab """
    login(browser)
    time.sleep(1)
    create_new_client(browser)
    delete_client(browser)
    
    
def test_edit_client(browser):
    """ Edit client from Projects tab """
    login(browser)
    time.sleep(1)
    page = get_projects_page(browser)
    create_new_client(browser)
    page.fill_client_search_field()
    page.click_edit_client_button()
    page.edit_client_name()
    page.edit_client_email()
    page.edit_client_phone()
    page.click_save_edit_client_button()
    delete_client(browser)
  