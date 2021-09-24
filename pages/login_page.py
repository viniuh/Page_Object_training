from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "#login_form" \
                                                                       "Login Username field is presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "#register_form" \
                                                                     "RegisterUsername field is presented"

    def register_new_user(self, email, password):
        email_locator = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_locator.send_keys(email)
        password_locator = self.browser.find_element(*LoginPageLocators.REG_PASS)
        password_locator.send_keys(password)
        passwd_confirm_locator = self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM)
        passwd_confirm_locator.send_keys(password)

    def click_reg_button(self):
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_btn.click()

    def should_be_success_reg_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REG_MESSAGE), "Registration message is absent"
