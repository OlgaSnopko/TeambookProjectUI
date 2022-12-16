from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/input')
    LAST_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/input')
    EMAIL = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/input')
    COMPANY_NAME = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div/div/input')
    PASSWORD = (By.ID, 'password_field')
    AGREEMENT_CHECKBOX = (By.XPATH, '//*[@id="marketing-accept-checkbox"]')
    CREATE_ORGANIZATION_BTN = (By.ID, 'create-account')


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')
    LOGIN_PASSWORD = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/input')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button > p')
    CREATE_BUTTON = (By.CLASS_NAME, 'login__input-side__login-link')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/p')


class ActualsPageLocators:
    CHOOSING_THE_DAY = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div')
    ADD_LOG_TIME = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/p[1]')
    POP_UP_WINDOW_BTN = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button')
    TIME_FIELD_FORM_ADD_NOTE = (By.NAME, 'estimated')
    PROJECT_FIELD_ADD_NOTE = (By.CSS_SELECTOR, '#selectProject > div > div > div:nth-of-type(2)')
    NOTES_FIELD_ADD_NOTE = (By.CLASS_NAME, 'time-logging-window__notes-textarea')
    BTN_ADD_NOTE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button')
    LINK_PAGE_ACTUALS = (By.LINK_TEXT, 'Actuals')
    NOTES_IN_CALENDAR = (By.CLASS_NAME, 'actuals__log-duration')
    SORT_USERS_BY_APPROVAL = (By.XPATH, '//div[@id="root"]/div[2]/div[2]/div/div[2]/p')
    SORT_USERS_BY_ALPHABET = (By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/p")
    SELECT_USER_EXAMPLE_2 = (By.CSS_SELECTOR, ".column-user__form:nth-child(2) > .column-user__user-info")
    SELECT_USER_EXAMPLE_1 = (By.CSS_SELECTOR, ".column-user__form:nth-child(3) > .column-user__user-info > p")
    SELECT_CURRENT_USER = (By.CSS_SELECTOR, ".column-user__form:nth-child(1) > .column-user__user-info")
    LEFT_ARROW = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/img[1]')
    RIGHT_ARROW = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/img[2]')
    CURRENT_DATE = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div/div/input')
    SELECT_YEAR = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div/div[121]')
    SELECT_MONTH = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div/div[5]')
    SELECT_TEAM_DROPDOWN = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[3]/div[1]/div')
    UNCHECK_TEAM = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li/span[1]/input')
    APPROVE_LOGS_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[3]/a')
    BULK_APPROVE_BTN = (By.CSS_SELECTOR, '.actuals__download-button:nth-child(2)')
    SELECT_USERS_DROPDOWN = (By.CSS_SELECTOR, '.copy-planner-select__value-container')
    SELECT_USER = (By.ID, 'react-select-2-option-2')
    BULK_APPROVE_SUBMIT_BTN = (By.CSS_SELECTOR, '.sc-kDDrLX > p')
    DOWNLOAD_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[3]/div[3]')
    SUBMIT_DOWNLOAD_BTN = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button')


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
    ARCHIVE_PROJECT_BTN = (By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/button/p[text()="Archive"]')
    FILTER_PROJECTS_BY_ACTIVITY = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]')
    SELECT_ARCHIVE_PROJECTS = (By.XPATH, '//div[text()="Archived"]')
    SELECT_ARCHIVE_PROJECT_CHECKBOX = (By.ID, 'selectProject')
    DELETE_ARCHIVE_PROJECT_ICON = (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/img[1]')
    DELETE_PROJECT_BTN = (By.XPATH, '//p[text()="Delete"]')
    MANAGE_CLIENTS_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/button[2]')
    CREATE_CLIENT_BTN = (By.ID, 'createClient')
    CLIENT_NAME = (By.ID, 'nameClient')
    CLIENT_EMAIL = (By.ID, 'emailClient')
    CLIENT_PHONE = (By.ID, 'phoneNumberClient')
    SAVE_CLIENT_BTN = (By.ID, 'saveClient')
    SEARCH_CLIENT_FIELD = (By.ID, ':rb:')
    EDIT_CLIENT_BTN = (By.ID, 'editClient')
    EDIT_CLIENT_NAME = (By.ID, 'editNameClient')
    EDIT_CLIENT_EMAIL = (By.ID, 'editEmailClient')
    EDIT_CLIENT_PHONE = (By.ID, 'editPhoneClient')
    SAVE_EDIT_CLIENT_BTN = (By.ID, 'saveEditClient')
    DELETE_CLIENT_ICON = (By.ID, 'deleteClient')
    DELETE_CLIENT_BTN = (By.XPATH, '//div[3]/div/div[2]/button/p')


class UsersPageLocators:
    CREATE_NEW_USER_BUTTON = (By.CSS_SELECTOR, "#root > div.App > div > div.filter-row > div.filter-row__right-side > "
                                               "button.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton"
                                               "-sizeMedium.MuiButton-textSizeMedium.MuiButtonBase-root.sc-kDDrLX.kjrQkc"
                                               ".mobile_hidden.filter-row__add-user-button.css-1ujsas3 > p > div > p")
    FIRST_NAME_BUTTON = (By.ID, 'userFirstName')
    LAST_NAME_BUTTON = (By.ID, 'userLastName')
    EMAIL_BUTTON = (By.ID, 'userEmail')
    TEAMS_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.form-create.css-126xj0f > "
                                     "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                     "div.MuiDialogContent-root.css-1ty026z > div.user-form__left-side > "
                                     "div.user-form__teams-select.creating > div > div > "
                                     "div.user-form__select-value__indicators.css-1wy0on6 > div > svg")
    CHOOSE_COMPANY = (By.ID, 'react-select-3-option-0')
    TAGS_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.form-create.css-126xj0f > "
                                    "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                    "div.MuiDialogContent-root.css-1ty026z > div.user-form__left-side > "
                                    "div.user-form__tags-select > div > div > "
                                    "div.user-form__select-value__indicators.css-1wy0on6 > div > svg")
    PHONE_NUMBER = (By.ID, 'userPhoneNumber')
    CREATE_BUTTON = (By.CSS_SELECTOR, "#createUser > p")
    OPEN_EDIT_FORM = (By.XPATH, "//p[contains(.,'Alla Vaserman')]")
    EDIT_USER_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.form-show.css-126xj0f > "
                                         "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                         "div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > button > p")
    USER_ROLE_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.form-edit.css-126xj0f > "
                                         "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                         "div.MuiDialogContent-root.css-1ty026z > div.user-form__right-side > "
                                         "div:nth-child(3) > div:nth-child(2) > div > div > "
                                         "div.user-form__select-value__indicators.css-1wy0on6 > div > svg")
    CHOOSE_USER_ROLE = (By.ID, 'react-select-6-option-1')
    SAVE_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.form-edit.css-126xj0f > "
                                    "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                    "div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > "
                                    "button.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium"
                                    ".MuiButton-textSizeMedium.MuiButtonBase-root.sc-kDDrLX.kjrQkc.user-form__edit"
                                    "-button.css-1ujsas3 > p")
    DELETE_BUTTON = (By.XPATH, "(//img[@ id='deleteUserButton'])[2]")

    DEACTIVATE_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.sc-idiyUo.bYuqGB.css-126xj0f > "
                                          "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                          "div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > "
                                          "button.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton"
                                          "-sizeMedium.MuiButton-textSizeMedium.MuiButtonBase-root.sc-kDDrLX.kjrQkc.css"
                                          "-1ujsas3 > p")
    ACTIVE_BUTTON = (By.CSS_SELECTOR, "#root > div.App > div > div.filter-row > div.filter-row__left-side > "
                                      "div.deactivate-dropdown__container > div > div > "
                                      "div.deactivate-dropdown__indicators.css-1wy0on6 > div > img")
    DEACTIVATE_DROPDOWN = (By.XPATH, "//div[@id='react-select-2-option-1']")
    SELECT_USER_FOR_ACTIVATE = (By.ID, 'selectUser')
    RACTIVATE_ICON = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-buttons > img:nth-child(3)")
    REACTIVATE_BUTTON = (By.CSS_SELECTOR, "body > div.MuiModal-root.MuiDialog-root.sc-idiyUo.bYuqGB.css-126xj0f > "
                                          "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                          "div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > "
                                          "button.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton"
                                          "-sizeMedium.MuiButton-textSizeMedium.MuiButtonBase-root.sc-kDDrLX.kjrQkc.css"
                                          "-1ujsas3 > p")

    EXPORT_BUTTON = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-buttons > img:nth-child(3)")
    CHECK_BOX_USER = (By.CSS_SELECTOR, "#selectUser")
    SORT_BY_NAME_BUTTON = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-content > "
                                            "div.users-page__user-list-header > "
                                            "div.users-page__user-list-header-value.name > div > p")
    SORT_BY_ROLE = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-content > "
                                     "div.users-page__user-list-header > div.users-page__user-list-header-value.role >"
                                     " div > p")
    FILTER_INPUT = (By.ID, 'filterUsers')
    OPEN_EDIT_FORM1 = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-content > "
                                        "div.users-page__user-list > div:nth-child(1) > div > "
                                        "div.users-block__avatar-container > p")
    DELETE_ICON = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-buttons > img:nth-child(1)")
    DELETE_BUTTON_IN_DELETE_FORM = (By.CSS_SELECTOR, ".MuiButton-text:nth-child(1) > p")
    SELECT_USER_CHECK_BOX = (By.ID, 'selectUser')
    DEACTIVATE_ICON = (By.CSS_SELECTOR, "#root > div.App > div > div.users-page__users-buttons > img:nth-child(2)")
