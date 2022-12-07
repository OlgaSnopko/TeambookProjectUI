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


class ActualsPageLocators:
    APPROVE_LOGS_BTN = (By.CSS_SELECTOR, '.dashboard__tb-button > p')
    BULK_APPROVE_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[3]/div[3]')
    SELECT_USERS_DROPDOWN = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div[3]/div[1]/div/div/div[1]')
    SELECT_USER = (By.ID, 'react-select-2-option-0')
    BULK_APPROVE_SUBMIT_BTN = (By.XPATH, '//div[2]/button/p')
