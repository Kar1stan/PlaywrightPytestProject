from playwright.sync_api import Page,expect


class TestProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_button = page.locator("//a[text()=' Products']")
        self.header_all_products = page.locator("//h2[text()='All Products']")
        self.products_list = page.locator("div[class='features_items']")
        self.view_product_button = page.locator("a[href='/product_details/1']")
        self.product_information = page.locator("div[class='product-information']")
        self.search_product_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.header_searcher_products = page.locator("//h2[text()='Searched Products']")
        self.add_cart_button = page.locator("a[data-product-id='1']").first
        self.continue_shopping_button = page.locator("//button[text()='Continue Shopping']")
        self.add_cart_second_product_button = page.locator("a[data-product-id='2']").first
        self.view_cart_button = page.locator("//u[text()='View Cart']")
        self.product_1 = page.locator("#product-1")
        self.product_2 = page.locator("#product-2")
        self.product_price = page.locator("td[class='cart_price']")
        self.product_quantity = page.locator("td[class='cart_quantity']")
        self.product_total_price = page.locator("td[class='cart_total']")
        self.quantity_input = page.locator("#quantity")
        self.add_cart_button_in_details = page.locator("#product_id~button")

    def click_products_button(self):
        self.products_button.click()

    def click_view_products_button(self):
        self.view_product_button.click()

    def fill_product_search(self, name):
        self.search_product_input.fill(name)

    def click_search_button(self):
        self.search_button.click()

    def click_add_cart_button(self):
        self.add_cart_button.hover()
        self.add_cart_button.click()

    def click_add_cart_second_product_button(self):
        self.add_cart_second_product_button.hover()
        self.add_cart_second_product_button.click()

    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

    def click_view_cart_button(self):
        self.view_cart_button.click()

    def fill_quantity_input(self, number):
        self.quantity_input.fill(number)

    def click_add_cart_button_in_details(self):
        self.add_cart_button_in_details.click()