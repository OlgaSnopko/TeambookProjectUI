import time
from utils.projects.get_projects_page import get_projects_page


def archive_project(browser, project_name):
    """ Function to archive a project """
    page = get_projects_page(browser)
    page.go_to_search_field(project_name)
    time.sleep(1)
    page.go_to_project_name_select()
    page.go_to_archive_project_icon()
    page.go_to_archive_project_button()
    