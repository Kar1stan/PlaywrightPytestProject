import pytest
from pages.user_registration_page import TestUserRegistrationPage
from playwright.sync_api import Page, expect
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAutomationExerciseSignup:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.registration = TestUserRegistrationPage(self.page)

    def test_case1_user_registration(self, test_before_each, page):
        """Should test signup registration with valid credentials and following deletion of account"""
        expect(page).to_be_visible()
        self.registration.click_signup_login_button()
        expect(self.registration.header_new_user_signup).to_be_visible()
        self.registration.fill_signup_name(Data.signup_name)
        self.registration.fill_signup_email(Data.signup_email)
        self.registration.click_signup_button()
        self.registration.check_title_button()
        expect(self.registration.header_enter_account_information).to_be_visible()
        self.registration.fill_signup_password(Data.signup_password)
        self.registration.choose_date_of_birth()
        self.registration.check_newsletter_button()
        self.registration.check_receive_special_offers_button()
        self.registration.fill_first_name(Data.signup_name)
        self.registration.fill_last_name(Data.signup_name)
        self.registration.fill_company(Data.signup_name)
        self.registration.fill_address("Imagined street")
        self.registration.fill_address2("Imagined street")
        self.registration.choose_country()
        self.registration.fill_state(Data.signup_name)
        self.registration.fill_city(Data.signup_name)
        self.registration.fill_zipcode(Data.zipcode)
        self.registration.fill_mobile_number(Data.zipcode)
        self.registration.click_create_account_button()
        expect(self.registration.header_account_created).to_be_visible()
        self.registration.click_continue_button()
        expect(self.registration.text_logged_as_username).to_be_visible()
        self.registration.click_delete_account_button()
        expect(self.registration.header_account_deleted).to_be_visible()
        self.registration.click_continue_button()
        take_screenshot(self.page, "case1:register_user")

    def test_case5_user_registration_with_existing_email(self, test_before_each, page):
        """Should test signup registration with already existing email"""
        expect(page).to_be_visible()
        self.registration.click_signup_login_button()
        expect(self.registration.header_new_user_signup).to_be_visible()
        self.registration.fill_signup_name(Data.signup_name)
        self.registration.fill_signup_email(Data.login_email)
        self.registration.click_signup_button()
        expect(self.registration.signup_error).to_be_visible()
        take_screenshot(self.page, "case5:register_user_with_existing_email")
