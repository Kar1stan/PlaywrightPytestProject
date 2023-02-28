import pytest
import re
from pages.test_cases_page import TestCasesPage
from playwright.sync_api import Page, expect
from utils.tools import take_screenshot


class TestAutomationExerciseTestCases:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.test_cases = TestCasesPage(self.page)

    def test_case7_verify_test_cases_page(self, test_before_each, page):
        """Should verify test cases page"""
        expect(self.page).to_be_visible()
        self.test_cases.click_test_cases_button()
        expect(self.page).to_have_url(re.compile("/test_cases$"))
        take_screenshot(self.page, "case7:verify_test_cases_page")
