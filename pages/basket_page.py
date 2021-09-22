from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage


class BasketPage(BasePage):
    def click_on_basket_btn(self):
        bask_btn = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON)
        bask_btn.click()

    def empty_basket(self):
        assert self.browser.find_element(*MainPageLocators.EMPTY_BASKET).text

    def should_not_be_quantity(self):
        assert self.is_not_element_present(*MainPageLocators.QUANTITY), \
            "The quantity is presented on empty basket page"


