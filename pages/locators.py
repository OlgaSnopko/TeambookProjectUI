from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/input')
    LAST_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/input')
    EMAIL = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/input')
    COMPANY_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/input')
    PASSWORD = (By.ID, 'password_field')
    AGREEMENT_CHECKBOX = (By.XPATH, "//span[@class='MuiCheckbox-root MuiCheckbox-colorPrimary MuiButtonBase-root "
                                    "MuiCheckbox-root MuiCheckbox-colorPrimary PrivateSwitchBase-root css-zun73v']")
    CREATE_ORGANIZATION_BTN = (By.ID, 'create-account')


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')
    LOGIN_PASSWORD = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/input')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button > p')
    CREATE_BUTTON = (By.CLASS_NAME, 'login__input-side__login-link')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/p')


class ActualsPageLocators:
    APPROVE_LOGS_BTN = (By.CSS_SELECTOR, '.dashboard__tb-button > p')
    BULK_APPROVE_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[3]/div[3]')
    SELECT_USERS_DROPDOWN = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div[3]/div[1]/div/div/div[1]')
    SELECT_USER = (By.ID, 'react-select-2-option-0')
    BULK_APPROVE_SUBMIT_BTN = (By.XPATH, '//div[2]/button/p')
    CHOOSING_THE_DAY = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div')
    ADD_LOG_TIME = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/p[1]')
    POP_UP_WINDOW_BTN = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button')
    TIME_FIELD_FORM_ADD_NOTE = (By.NAME, 'estimated')
    PROJECT_FIELD_ADD_NOTE = (By.CSS_SELECTOR, '#selectProject > div > div > div:nth-of-type(2)')
    NOTES_FIELD_ADD_NOTE = (By.CLASS_NAME, 'time-logging-window__notes-textarea')
    BTN_ADD_NOTE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button')
    LINK_PAGE_ACTUALS = (By.LINK_TEXT, 'Actuals')
    NOTES_IN_CALENDAR = (By.CLASS_NAME, 'actuals__log-duration')


class ProjectsPageLocators:
    CREATE_PROJECT_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div/button')
    PROJECT_NAME = (By.ID, 'projectName')
    PROJECT_SHORT_NAME = (By.ID, 'projectShortName')
    CLIENT = (By.XPATH, '//*[@id="tags-outlined"]/div')
    SELECT_CLIENT = (By.ID, 'react-select-3-option-0')
    BILLABLE = (By.XPATH, '//*[@id="selectBillable"]/div/div[1]/div[2]')
    ESTIMATED_HOURS = (By.ID, 'estimated')
    MANAGER = (By.XPATH, '//div[3]/div[2]/p[2]/div/div/div')
    SELECT_MANAGER = (By.ID, 'react-select-5-option-2')
    STATUS = (By.XPATH, '//p[../p[text()="Status"]]/div')
    SELECT_STATUS = (By.XPATH, '//*[text()="Done"]')
    BUSINESS_UNIT = (By.XPATH, '//div[4]/div[2]/p[2]/div/div/div/input')
    DEFINE_START_END_DATES_CHECKBOX = (By.XPATH, '//span/input')
    PROJECT_COLOR = (By.CSS_SELECTOR, '.project-form__project-color')
    SELECT_PROJECT_COLOR = (By.CSS_SELECTOR, 'span:nth-child(8) > div div')
    CREATE_BTN = (By.XPATH, '//*[@id="createProject"]')
    SEARCH_FIELD = (By.ID, 'filterProjects')
    PROJECT_NAME_SELECT = (By.XPATH, '//*[@id="root"]/div[2]/div/div[4]/div[2]/div/div/div[2]/p')
    ARCHIVE_PROJECT_ICON = (By.ID, 'deleteProjectButton')
    ARCHIVE_PROJECT_BTN = (By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary '
                                     'MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root sc-kDDrLX '
                                     'kjrQkc css-1ujsas3"]')
    FILTER_PROJECTS_BY_ACTIVITY = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]')
    SELECT_ARCHIVE_PROJECTS = (By.XPATH, '//div[text()="Archived"]')
    SELECT_ARCHIVE_PROJECT_CHECKBOX = (By.ID, 'selectProject')
    DELETE_ARCHIVE_PROJECT_ICON = (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/img[1]')
    DELETE_PROJECT_BTN = (By.XPATH, '//p[text()="Delete"]')
    
    