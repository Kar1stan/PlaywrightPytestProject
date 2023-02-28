import pytest
import re
from pages.home_page import TestHomePage
from playwright.sync_api import Page, expect
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAutomationExerciseHome:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.home = TestHomePage(self.page)

    def test_case10_verify_subscription(self, test_before_each, page):
        """Should verify subscription in home page"""
        expect(self.page).to_be_visible()
        self.home.scroll_to_footer()
        expect(self.home.header_subscription).to_be_visible()
        self.home.fill_email_input(Data.signup_email)
        self.home.click_subscription_button()
        expect(self.home.subscription_success_message).to_be_visible()
        take_screenshot(self.page, "case10:verify subscription in home page")