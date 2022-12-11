from utils.projects.get_projects_page import get_projects_page


def create_project(browser, project_name, project_short_name):
    """ Function to create a new project """
    page = get_projects_page(browser)
    page.go_to_create_project_button()
    page.go_to_project_name(project_name)
    page.go_to_project_short_name(project_short_name)
    page.go_to_client()
    page.go_to_select_client()
    page.go_to_estimated_hours()
    page.go_to_manager()
    page.go_to_select_manager()
    page.go_to_status()
    page.go_to_business_unit()
    page.go_to_define_start_end_dates_checkbox()
    page.go_to_project_color()
    page.go_to_select_project_color()
    page.go_to_create_button()
    