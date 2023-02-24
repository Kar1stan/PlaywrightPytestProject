import pytest
from pages.user_registration_page import TestUserRegistrationPage
from pages.contact_us_page import TestContactUsPage
from playwright.sync_api import Page, expect
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAutomationExerciseContactUs:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.registration = TestUserRegistrationPage(self.page)
        self.contact_us = TestContactUsPage(self.page)

    def test_case6_contact_us_form_with_valid_credentials(self, test_before_each, page):
        """Should test contact us with valid credentials"""
        expect(page).to_be_visible()
        self.contact_us.click_contact_us_button()
        expect(self.contact_us.header_get_in_touch).to_be_visible()
        self.contact_us.fill_name(Data.signup_name)
        self.contact_us.fill_email(Data.signup_email)
        self.contact_us.fill_subject(Data.signup_name)
        self.contact_us.fill_message(Data.signup_name)
        self.contact_us.click_submit_button()