from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMPTY_BASKET = (By.XPATH, "//div[@id ='content_inner']//p")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>.btn:nth-child(1)")
    QUANTITY = (By.CSS_SELECTOR, '[type="number]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".col-sm-6>h1")
    TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1)>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")