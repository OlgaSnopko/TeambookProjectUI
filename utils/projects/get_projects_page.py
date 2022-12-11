from pages.projects_page import ProjectsPage
from pages.settings import url_projects_page


def get_projects_page(browser):
	""" Function to get projects page """
	link = url_projects_page
	page = ProjectsPage(browser, link)
	page.open()
	return page
