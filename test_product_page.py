import time
import faker
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from.pages.basket_page import BasketPage


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email1 = f.email()
        password1 = "!QAZ2wsx#EDC"
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        page.should_be_register_form()
        page.register_new_user(email1, password1)
        page.click_reg_button()
        page.success_reg_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_basket()
        page.add_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_be_book_name()
    page.add_to_basket()
    page.solve_quiz_and_get_code()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.click_on_basket_btn()
    page.empty_basket()
    page.should_not_be_quantity()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    time.sleep(5)









    """def test_message_disappeared_after_adding_product_to_basket(self, browser):
        browser.delete_all_cookies()
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_basket()
        page.should_be_book_name()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.verify_text()
        page.test_message_disappeared_after_adding_product()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(5)


@pytest.mark.skip
d


"""







"""def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_be_book_name()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.verify_text()
    page.test_guest_cant_see_success_message_after_adding_product()
    """




















"""


    def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_basket()
        page.should_be_book_name()
        page.add_to_basket()
        page.solve_quiz_and_get_code()"""