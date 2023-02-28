from playwright.sync_api import Page


class TestHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.footer = page.locator("#footer")
        self.header_subscription = page.locator("//h2[text()='Subscription']")
        self.email_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_success_message = page.locator("#success-subscribe")

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def fill_email_input(self, email):
        self.email_input.fill(email)

    def click_subscription_button(self):
        self.subscription_button.click()