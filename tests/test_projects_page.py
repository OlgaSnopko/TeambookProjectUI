import time
from utils.login import login
from utils.projects.archive_project import archive_project
from utils.projects.create_project import create_project
from utils.projects.delete_project import delete_project


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
  
    
    