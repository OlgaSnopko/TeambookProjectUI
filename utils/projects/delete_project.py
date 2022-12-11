import time
from utils.projects.get_projects_page import get_projects_page


def delete_project(browser, project_name):
    """ Function to delete a project after archiving """
    page = get_projects_page(browser)
    page.go_to_search_field(project_name)
    time.sleep(1)
    page.go_to_filter_project_by_activity()
    page.go_to_select_archive_projects()
    page.go_to_select_archive_project_checkbox()
    page.go_to_delete_archive_project_icon()
    page.go_to_delete_project_button()
