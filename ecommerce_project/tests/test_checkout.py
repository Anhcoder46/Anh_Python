import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.credentials import VALID_USERNAME, VALID_PASSWORD


class TestCheckoutProcess:
    def test_complete_checkout_with_valid_info(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)

        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()

        assert checkout_page.get_overview_items(), "Should have items on overview"

        checkout_page.click_finish()

        assert checkout_page.is_order_complete(), "Order should be completed"

    def test_checkout_with_single_product(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        product_names = inventory_page.get_all_product_names()
        product_to_add = product_names[0]
        inventory_page.add_product_by_name(product_to_add)

        inventory_page.click_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Jane", "Smith", "54321")
        checkout_page.click_continue()

        assert checkout_page.is_item_in_overview(product_to_add), \
            f"{product_to_add} should be in overview"

        checkout_page.click_finish()
        assert checkout_page.is_order_complete(), "Order should be completed"

    def test_checkout_with_multiple_products(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        product_names = inventory_page.get_all_product_names()
        products_to_add = product_names[:3]

        for product in products_to_add:
            inventory_page.add_product_by_name(product)

        inventory_page.click_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Bob", "Johnson", "99999")
        checkout_page.click_continue()

        for product in products_to_add:
            assert checkout_page.is_item_in_overview(product), \
                f"{product} should be in overview"

        checkout_page.click_finish()
        assert checkout_page.is_order_complete(), "Order should be completed"

    def test_checkout_verify_order_details_on_overview(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)

        product_names = inventory_page.get_all_product_names()[:2]

        inventory_page.click_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Alice", "Wonder", "11111")
        checkout_page.click_continue()

        items = checkout_page.get_overview_items()
        assert len(items) >= 2, "Should have at least 2 items in overview"

        for product_name in product_names:
            assert checkout_page.is_item_in_overview(product_name), \
                f"{product_name} should be visible in overview"

class TestCheckoutValidation:
    def test_checkout_missing_first_name(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_zip_code("12345")
        checkout_page.click_continue()

        assert checkout_page.is_error_displayed(), "Error should be displayed"

    def test_checkout_missing_last_name(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_zip_code("12345")
        checkout_page.click_continue()

        assert checkout_page.is_error_displayed(), "Error should be displayed"

    def test_checkout_missing_zip_code(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.click_continue()

        assert checkout_page.is_error_displayed(), "Error should be displayed"

    def test_checkout_all_fields_empty(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.click_continue()

        assert checkout_page.is_error_displayed(), "Error should be displayed for empty fields"

    def test_checkout_with_special_characters_in_name(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John-Paul", "O'Reilly", "12345")
        checkout_page.click_continue()

        overview_items = checkout_page.get_overview_items()
        assert len(overview_items) > 0, "Should proceed to overview with special chars in name"

    def test_checkout_correct_info_after_error(self, driver):
        """Test checkout with correct info after initial error"""
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.click_continue()

        assert checkout_page.is_error_displayed(), "Error should display for incomplete info"

        checkout_page.enter_last_name("Doe")
        checkout_page.enter_zip_code("12345")
        checkout_page.click_continue()

        overview_items = checkout_page.get_overview_items()
        assert len(overview_items) > 0, "Should proceed after filling all fields"
