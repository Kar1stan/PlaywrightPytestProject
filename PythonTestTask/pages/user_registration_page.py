from playwright.sync_api import Page


class TestUserRegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_login_button = page.locator('a[href="/login"]')
        self.header_new_user_signup = page.locator("//h2[text()='New User Signup!']")
        self.signup_name_input = page.locator("input[data-qa='signup-name']")
        self.signup_email_input = page.locator("input[data-qa='signup-email']")
        self.signup_password_input = page.locator("input[data-qa='password']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        self.header_enter_account_information = page.locator("//b[text()='Enter Account Information']")
        self.mr_check_button = page.locator("#id_gender1")
        self.day_of_birth = page.locator("#days")
        self.month_of_birth = page.locator("#months")
        self.year_of_birth = page.locator("#years")
        self.signup_newsletter_button = page.locator("#newsletter")
        self.receive_special_offers_button = page.locator("#optin")
        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_input = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.locator("#mobile_number")
        self.create_account_button = page.locator("button[data-qa='create-account']")
        self.header_account_created = page.locator("//b[text()='Account Created!']")
        self.continue_button = page.locator("a[data-qa='continue-button']")
        self.text_logged_as_username = page.locator("//a[text()=' Logged in as ']")
        self.delete_account_button = page.locator("//a[text()=' Delete Account']")
        self.header_account_deleted = page.locator("//b[text()='Account Deleted!']")
        self.signup_error = page.locator("//p[text()='Email Address already exist!']")

    def click_signup_login_button(self):
        self.signup_login_button.click()

    def fill_signup_name(self, name):
        self.signup_name_input.fill(name)

    def fill_signup_email(self, email):
        self.signup_email_input.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def check_title_button(self):
        self.mr_check_button.check()

    def fill_signup_password(self, password):
        self.signup_password_input.fill(password)

    def choose_date_of_birth(self):
        self.day_of_birth.select_option("7")
        self.year_of_birth.select_option("1998")
        self.month_of_birth.select_option("March")

    def check_newsletter_button(self):
        self.signup_newsletter_button.check()

    def check_receive_special_offers_button(self):
        self.receive_special_offers_button.check()

    def fill_first_name(self, name):
        self.first_name_input.fill(name)

    def fill_last_name(self, name):
        self.last_name_input.fill(name)

    def fill_company(self, company_name):
        self.company_input.fill(company_name)

    def fill_address(self, address):
        self.address_input.fill(address)

    def fill_address2(self, address):
        self.address2_input.fill(address)

    def choose_country(self):
        self.country_input.select_option("Israel")

    def fill_state(self, state_name):
        self.state_input.fill(state_name)

    def fill_city(self, city_name):
        self.city_input.fill(city_name)

    def fill_zipcode(self, zipcode):
        self.zipcode_input.fill(zipcode)

    def fill_mobile_number(self, mobile_number):
        self.mobile_number_input.fill(mobile_number)

    def click_create_account_button(self):
        self.create_account_button.scroll_into_view_if_needed()
        self.create_account_button.click()

    def click_continue_button(self):
        self.continue_button.click()

    def click_delete_account_button(self):
        self.delete_account_button.click()
