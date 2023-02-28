from playwright.sync_api import Page


class TestContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_us_button = page.locator("//a[text()=' Contact us']")
        self.header_get_in_touch = page.locator("//h2[text()='Get In Touch']")
        self.name_input = page.locator("input[data-qa='name']")
        self.email_input = page.locator("input[data-qa='email']")
        self.subject_input = page.locator("input[data-qa='subject']")
        self.message_input = page.locator("#message")
        self.file_input = page.locator("input[name='upload_file']")
        self.submit_button = page.locator("input[data-qa='submit-button']")

    def click_contact_us_button(self):
        self.contact_us_button.click()

    def fill_name(self, name):
        self.name_input.fill(name)

    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_subject(self, subject):
        self.subject_input.fill(subject)

    def fill_message(self, message):
        self.message_input.fill(message)

    def click_submit_button(self):
        self.submit_button.click()

    def upload_file(self):
        self.file_input.set_input_files("./images/birds.png")