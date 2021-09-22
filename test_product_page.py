import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(5)


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    time.sleep(5)


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.click_on_basket_btn()
    page.empty_basket()
    page.should_not_be_quantity()






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


def test_guest_cant_see_success_message(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_be_book_name()
    page.test_guest_cant_see_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_be_book_name()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.verify_text()
    page.test_message_disappeared_after_adding_product()"""














"""@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser,link):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.should_add_to_basket()
    page.should_be_book_name()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.verify_text()


    def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_basket()
        page.should_be_book_name()
        page.add_to_basket()
        page.solve_quiz_and_get_code()"""