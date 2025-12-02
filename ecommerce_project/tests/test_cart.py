import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.credentials import VALID_USERNAME, VALID_PASSWORD

class TestAddToCart:
    def test_add_single_product_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)
        initial_badge = inventory_page.get_cart_badge_count()
        inventory_page.add_product_to_cart(0)
        new_badge = inventory_page.get_cart_badge_count()
        assert new_badge == initial_badge + 1, "Cart badge should increase by 1"

    def test_add_multiple_products_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        inventory_page = InventoryPage(driver)

        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        inventory_page.add_product_to_cart(2)

        badge_count = inventory_page.get_cart_badge_count()
        assert badge_count == 3, "Cart should have 3 items"

    def test_product_appears_in_cart_page(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        product_names = inventory_page.get_all_product_names()
        product_to_add = product_names[0]

        inventory_page.add_product_by_name(product_to_add)

        inventory_page.click_cart()
        cart_page = CartPage(driver)

        cart_items = cart_page.get_cart_item_names()
        assert product_to_add in cart_items, f"{product_to_add} should be in cart"

    def test_add_multiple_different_products_verify_in_cart(self, driver):
        """Test adding multiple different products and verify in cart"""
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        product_names = inventory_page.get_all_product_names()
        products_to_add = product_names[:3]

        for product in products_to_add:
            inventory_page.add_product_by_name(product)

        inventory_page.click_cart()
        cart_page = CartPage(driver)

        cart_items = cart_page.get_cart_item_names()
        for product in products_to_add:
            assert product in cart_items, f"{product} should be in cart"

        assert cart_page.get_item_count() == 3, "Cart should have 3 items"

class TestRemoveFromCart:
    def test_remove_product_from_cart_page(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        product_names = inventory_page.get_all_product_names()
        product_to_add = product_names[0]

        inventory_page.add_product_by_name(product_to_add)
        initial_count = inventory_page.get_cart_badge_count()

        inventory_page.click_cart()
        cart_page = CartPage(driver)

        cart_page.remove_item_by_name(product_to_add)

        assert cart_page.is_cart_empty(), "Cart should be empty after removing item"

    def test_remove_product_from_inventory_page(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        initial_badge = inventory_page.get_cart_badge_count()

        inventory_page.remove_product(0)

        new_badge = inventory_page.get_cart_badge_count()
        assert new_badge == initial_badge - 1, "Badge count should decrease by 1"

    def test_remove_one_of_multiple_products(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        product_names = inventory_page.get_all_product_names()

        inventory_page.add_product_by_name(product_names[0])
        inventory_page.add_product_by_name(product_names[1])
        inventory_page.add_product_by_name(product_names[2])

        inventory_page.click_cart()
        cart_page = CartPage(driver)

        cart_page.remove_item_by_name(product_names[1])

        remaining_items = cart_page.get_cart_item_names()
        assert len(remaining_items) == 2, "Should have 2 items remaining"
        assert product_names[1] not in remaining_items, "Removed item should not be in cart"
        assert product_names[0] in remaining_items, "First item should still be in cart"
        assert product_names[2] in remaining_items, "Third item should still be in cart"

    def test_cart_updates_reflect_on_badge(self, driver):
        login_page = LoginPage(driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)

        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        inventory_page.add_product_to_cart(2)

        assert inventory_page.get_cart_badge_count() == 3

        inventory_page.remove_product(0)
        assert inventory_page.get_cart_badge_count() == 2

        inventory_page.remove_product(1)
        assert inventory_page.get_cart_badge_count() == 1