from playwright.sync_api import Page


class TestLoginUserPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_login_to_your_account = page.locator("//h2[text()='Login to your account']")
        self.login_email_input = page.locator("input[data-qa='login-email']")
        self.login_password_input = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.login_error = page.locator("//p[text()='Your email or password is incorrect!']")
        self.logout_button = page.locator("//a[text()=' Logout']")

    def fill_login_email(self, email):
        self.login_email_input.fill(email)

    def fill_login_password(self, password):
        self.login_password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def click_logout_button(self):
        self.logout_button.click()