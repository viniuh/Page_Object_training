import time
import  pytest
from .pages.product_page import ProductPage


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

    """def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_basket()
        page.should_be_book_name()
        page.add_to_basket()
        page.solve_quiz_and_get_code()"""