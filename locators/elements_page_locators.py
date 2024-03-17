
from selenium.webdriver.common.by import By


class ElementLocators:

    LOG_AND_PASS = (By.CSS_SELECTOR, 'div.form__input-wrapper input')
    NEXT1 = (By.CSS_SELECTOR, 'div.auth__submitButton button')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'div.upload__dropzone input:nth-child(1)')
    NEXT2 = (By.CSS_SELECTOR, 'div.wizardSignForm-createButton button:enabled')
    SIGN_SEND = (By.CSS_SELECTOR, 'div.radio-button__wrapper:nth-child(2) label')
    ADD_SIGNERS = (By.CSS_SELECTOR, 'div.wizardSignForm__signersContainer svg')
    ADD_VIEWERS = (By.CSS_SELECTOR, 'div.signTemplate__emailField svg')
    SIGNERS_NAME_EMAIL = (By.CSS_SELECTOR, 'div.wizardSignForm__signerItem input')
    VIEWERS_EMAIL = (By.CSS_SELECTOR, 'div.emailRecipients__item-inner input')
    NEXT3 = (By.CSS_SELECTOR, 'form.wizardSignForm__form button:enabled')
    GOT_IT = (By.CSS_SELECTOR, 'div.text-tooltip__independent button')
    ALL_FIELDS = (By.CSS_SELECTOR, 'ul.interactModal__fieldBar-fieldList Li')
    CANVAS = (By.CSS_SELECTOR, 'div.documentPage__inner-pdf_page canvas')
    SIGNATURE = (By.CSS_SELECTOR, 'span.fieldDropDown__requisite-blank-title')
    ME = (By.CSS_SELECTOR, 'Li.fieldDropDown__item:nth-child(2)')
    SPISOK_ME_OLD = (By.CSS_SELECTOR, 'div.settingsSignature__dropDown-trigger')
    DELETE_ME_PLD = (By.CSS_SELECTOR, 'div.settingsSignature__dropDown-item--delete')
    DELETE_ACCEPT = (By.CSS_SELECTOR, 'button.button--red')
    CREATE_NOW = (By.CSS_SELECTOR, 'p.requisiteModal__custom-signature span')
    OPEN_FONT = (By.CSS_SELECTOR, 'div.requisiteModal__type-select div.uiSelect__select')
    LIST_FONT = (By.CSS_SELECTOR, 'div.uiSelect__search-item')
    I_AGREE = (By.CSS_SELECTOR, 'footer.requisiteModal__footer div.uiCheckbox__inner')
    NEXT4 = (By.CSS_SELECTOR, 'footer.requisiteModal__footer button:enabled')
    SAVE = (By.CSS_SELECTOR, 'div.interactModal__header-send button:nth-child(2)')
    SIGN_A_DOCUMENT = (By.CSS_SELECTOR, 'button[type="submit"]')














