import time
from pages.projects_page import ProjectsPage
from pages.settings import url_projects_page


def get_projects_page(browser):
	""" Function to get projects_page page """
	link = url_projects_page
	page = ProjectsPage(browser, link)
	page.open()
	return page


def create_project(browser, project_name, project_short_name):
	""" Function to create a new project """
	page = get_projects_page(browser)
	page.click_create_project_button()
	page.fill_project_name(project_name)
	page.fill_project_short_name(project_short_name)
	page.click_client_field()
	page.select_client()
	page.fill_estimated_hours()
	page.click_manager_field()
	page.select_manager()
	page.select_status()
	page.fill_business_unit()
	page.click_define_start_end_dates_checkbox()
	page.click_project_color()
	page.select_project_color()
	page.click_create_button()


def archive_project(browser, project_name):
	""" Function to archive a project """
	page = get_projects_page(browser)
	page.fill_project_search_field(project_name)
	time.sleep(1)
	page.select_project_name()
	page.click_archive_project_icon()
	page.click_archive_project_button()


def delete_project(browser, project_name):
	""" Function to delete a project after archiving """
	page = get_projects_page(browser)
	page.fill_project_search_field(project_name)
	time.sleep(1)
	page.filter_project_by_activity()
	page.select_archive_projects()
	page.click_archive_project_checkbox()
	page.click_delete_archive_project_icon()
	page.click_delete_project_button()
