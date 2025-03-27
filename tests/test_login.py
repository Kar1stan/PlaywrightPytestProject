import pytest
import re
from pages.login_user_page import TestLoginUserPage
from pages.user_registration_page import TestUserRegistrationPage
from playwright.sync_api import Page, expect
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAutomationExerciseLogin:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.login = TestLoginUserPage(self.page)
        self.registration = TestUserRegistrationPage(self.page)

    def test_case2_login_user_with_correct_credentials(self, test_before_each, page):
        """Should test login user with valid credentials and following deletion of account"""
        expect(self.page).to_be_visible()
        self.registration.click_signup_login_button()
        expect(self.login.header_login_to_your_account).to_be_visible()
        self.login.fill_login_email(Data.login_email)
        self.login.fill_login_password(Data.login_password)
        self.login.click_login_button()
        expect(self.registration.text_logged_as_username).to_be_visible()
        self.registration.click_delete_account_button()
        expect(self.registration.header_account_deleted).to_be_visible()
        take_screenshot(self.page, "case2:login_user_with_valid_credentials")

    def test_case3_login_user_with_incorrect_credentials(self, test_before_each, page):
        """Should test login user with incorrect credentials"""
        expect(self.page).to_be_visible()
        self.registration.click_signup_login_button()
        expect(self.login.header_login_to_your_account).to_be_visible()
        self.login.fill_login_email(Data.incorrect_login_email)
        self.login.fill_login_password(Data.incorrect_login_password)
        self.login.click_login_button()
        expect(self.login.login_error).to_be_visible()
        take_screenshot(self.page, "case3:login_user_with_incorrect_credentials")

    def test_case4_logout_user(self, test_before_each, page):
        """Should test user logout"""
        expect(self.page).to_be_visible()
        self.registration.click_signup_login_button()
        expect(self.login.header_login_to_your_account).to_be_visible()
        self.login.fill_login_email(Data.login_email)
        self.login.fill_login_password(Data.login_password)
        self.login.click_login_button()
        expect(self.registration.text_logged_as_username).to_be_visible()
        self.login.click_logout_button()
        expect(self.page).to_have_url(re.compile("/login$"))
        take_screenshot(self.page, "case4:user_logout")
