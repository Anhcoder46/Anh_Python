import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.credentials import VALID_USERNAME, VALID_PASSWORD

class TestProductSorting:
    def test_sort_by_name_a_to_z(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.sort_by("az")
        product_names = inventory_page.get_all_product_names()
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, "Products should be sorted A-Z"

    def test_sort_by_name_z_to_a(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)
        inventory_page.sort_by("za")
        product_names = inventory_page.get_all_product_names()
        sorted_names = sorted(product_names, reverse=True)
        assert product_names == sorted_names, "Products should be sorted Z-A"

    def test_sort_by_price_low_to_high(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)
        inventory_page.sort_by("lohi")
        product_prices = inventory_page.get_all_product_prices()
        sorted_prices = sorted(product_prices)
        assert product_prices == sorted_prices, "Products should be sorted by price low-high"

    def test_sort_by_price_high_to_low(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)
        inventory_page.sort_by("hilo")
        product_prices = inventory_page.get_all_product_prices()
        sorted_prices = sorted(product_prices, reverse=True)
        assert product_prices == sorted_prices, "Products should be sorted by price high-low"

    def test_sort_maintains_product_information(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)
        initial_count = len(inventory_page.get_all_products())
        inventory_page.sort_by("az")
        sorted_count = len(inventory_page.get_all_products())
        assert initial_count == sorted_count, "Product count should remain same after sorting"

        prices = inventory_page.get_all_product_prices()
        assert len(prices) == initial_count, "All products should have prices"

    def test_switch_between_sort_options(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)
        original_names = inventory_page.get_all_product_names()
        inventory_page.sort_by("az")
        az_names = inventory_page.get_all_product_names()
        inventory_page.sort_by("lohi")
        lohi_prices = inventory_page.get_all_product_prices()
        inventory_page.sort_by("az")
        az_names_again = inventory_page.get_all_product_names()
        assert az_names == az_names_again, "A-Z sort should be consistent"
        assert lohi_prices == sorted(lohi_prices), "Should be sorted low-high"
