import pytest
import re
from pages.cart_page import TestCartPage
from playwright.sync_api import Page, expect
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAutomationExerciseTestCases:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.cart = TestCartPage(self.page)

    def test_case11_verify_subscription(self, test_before_each, page):
        """Should verify subscription in cart page"""
        expect(self.page).to_be_visible()
        self.cart.click_cart_button()
        self.cart.scroll_to_footer()
        expect(self.cart.header_subscription).to_be_visible()
        self.cart.fill_email_input(Data.signup_email)
        self.cart.click_subscription_button()
        expect(self.cart.subscription_success_message).to_be_visible()
        take_screenshot(self.page, "case11:verify subscription in cart page")
