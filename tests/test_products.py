import pytest
import re
from pages.products_page import TestProductsPage
from playwright.sync_api import Page, expect
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAutomationExerciseProducts:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.products = TestProductsPage(self.page)

    def test_case8_verify_products_page(self, test_before_each, page):
        """Should verify test cases page"""
        expect(self.page).to_be_visible()
        self.products.click_products_button()
        expect(self.products.header_all_products).to_be_visible()
        expect(self.products.products_list).to_be_visible()
        self.products.click_view_products_button()
        expect(self.products.product_information).to_be_visible()
        expect(self.page).to_have_url(re.compile("/product_details/"))
        take_screenshot(self.page, "case8:verify_products_page and product detail page")

    def test_case9_search_products(self, test_before_each, page):
        """Should test search in products page"""
        expect(self.page).to_be_visible()
        self.products.click_products_button()
        expect(self.products.header_all_products).to_be_visible()
        self.products.fill_product_search(Data.search_product)
        self.products.click_search_button()
        expect(self.products.header_searcher_products).to_be_visible()
        expect(self.products.products_list).to_be_visible()
        take_screenshot(self.page, "case9:search in products page")

    def test_case12_add_products_in_cart(self, test_before_each, page):
        """Should add products in cart"""
        expect(self.page).to_be_visible()
        self.products.click_products_button()
        self.products.click_add_cart_button()
        self.products.click_continue_shopping_button()
        self.products.click_add_cart_second_product_button()
        self.products.click_view_cart_button()
        expect(self.products.product_1).to_be_visible()
        expect(self.products.product_2).to_be_visible()
        expect(self.products.product_price.first).to_be_visible()
        expect(self.products.product_quantity.first).to_be_visible()
        expect(self.products.product_total_price.first).to_be_visible()
        expect(self.products.product_price.second).to_be_visible()
        expect(self.products.product_quantity.second).to_be_visible()
        expect(self.products.product_total_price.second).to_be_visible()
        take_screenshot(self.page, "case12:add products in cart")

    @pytest.mark.one
    def test_case13_verify_product_quantity_in_cart(self, test_before_each, page):
        """Should verify product quantity in cart page"""
        expect(self.page).to_be_visible()
        self.products.click_view_products_button()
        expect(self.page).to_have_url(re.compile("/product_details/"))
        self.products.fill_quantity_input("4")
        self.products.click_add_cart_button_in_details()
        self.products.click_view_cart_button()
        expect(self.products.product_quantity).to_contain_text("4")
        take_screenshot(self.page, "case13:verify product quantity in cart page")