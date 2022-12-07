from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/input')
    LAST_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/input')
    EMAIL = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/input')
    COMPANY_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/input')
    PASSWORD = (By.ID, "password_field")
    AGREEMENT_CHECKBOX = (By.XPATH, "//span[@class='MuiCheckbox-root MuiCheckbox-colorPrimary MuiButtonBase-root "
                                    "MuiCheckbox-root MuiCheckbox-colorPrimary PrivateSwitchBase-root css-zun73v']")
    CREATE_ORGANIZATION_BTN = (By.ID, 'create-account')
