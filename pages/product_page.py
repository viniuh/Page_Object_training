from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            "The Add_to_basket button is not presented"

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_TITLE), \
                    "Book title in not presented"

    def should_be_verifying_text_first(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_TITLE_TEXT_SUCCESS).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text, "Title texts aren't matching"

    def should_be_success_div(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_DIV), \
            "Something wrong with the success div"

    def test_guest_cant_see_success_message_after_adding_product(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")




