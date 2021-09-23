from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_login_form(self, browser):
        link1 = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link1)
        page.open()
        page.should_be_login_url()
        page.should_be_login_form()
        page.should_be_register_form()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.click_on_basket_btn()
        page.empty_basket()
        page.should_not_be_quantity()





