from selenium.webdriver import Keys


def clear_field(field):
	field.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
	return field
