from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()




def test_login_form(browser):
    link1 = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link1)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

