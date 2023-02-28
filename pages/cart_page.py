from playwright.sync_api import Page


class TestCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_button = page.locator("//a[text()=' Cart']")
        self.header_subscription = page.locator("//h2[text()='Subscription']")
        self.footer = page.locator("#footer")
        self.email_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_success_message = page.locator("#success-subscribe")

    def click_cart_button(self):
        self.cart_button.click()

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def fill_email_input(self, email):
        self.email_input.fill(email)

    def click_subscription_button(self):
        self.subscription_button.click()