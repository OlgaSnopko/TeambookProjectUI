from utils.projects_page.projects import get_projects_page


def create_new_client(browser):
	""" Function to create a new client from Projects tab """
	page = get_projects_page(browser)
	page.click_manage_clients_button()
	page.click_create_client_button()
	page.fill_client_name()
	page.fill_client_email()
	page.fill_client_phone()
	page.click_save_client_button()
	
	
def delete_client(browser):
	""" Function to create a new client from Projects tab """
	page = get_projects_page(browser)
	page.click_manage_clients_button()
	page.fill_client_search_field()
	page.click_delete_client_icon()
	page.click_delete_client_button()
