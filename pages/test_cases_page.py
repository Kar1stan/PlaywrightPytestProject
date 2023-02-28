from playwright.sync_api import Page


class TestCasesPage:
    def __init__(self, page: Page):
        self.page = page
        self.test_cases_button = page.locator("//a[text()=' Test Cases']")

    def click_test_cases_button(self):
        self.test_cases_button.click()