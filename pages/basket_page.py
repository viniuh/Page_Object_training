from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def click_on_basket_btn(self):
        bask_btn = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON)
        bask_btn.click()

    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*MainPageLocators.EMPTY_BASKET).text

    def should_not_be_quantity(self):
        assert self.is_not_element_present(*MainPageLocators.QUANTITY_OF_BOOKS), \
            "The quantity is presented on empty basket page"


