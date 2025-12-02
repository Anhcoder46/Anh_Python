from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for Inventory/Products page"""

    # Locators
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def get_all_products(self):
        """Get all product elements"""
        return self.find_all(self.PRODUCT_ITEMS)

    def add_product_to_cart(self, product_index=0):
        """Add product to cart by index"""
        products = self.get_all_products()
        add_button = products[product_index].find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()

    def add_product_by_name(self, product_name):
        """Add product to cart by product name"""
        products = self.get_all_products()
        for product in products:
            name = product.find_element(*self.PRODUCT_NAME).text
            if name == product_name:
                button = product.find_element(*self.ADD_TO_CART_BUTTON)
                button.click()
                return True
        return False

    def remove_product(self, product_index=0):
        """Remove product from cart by index"""
        products = self.get_all_products()
        remove_button = products[product_index].find_element(*self.REMOVE_BUTTON)
        remove_button.click()

    def remove_product_by_name(self, product_name):
        """Remove product by name"""
        products = self.get_all_products()
        for product in products:
            name = product.find_element(*self.PRODUCT_NAME).text
            if name == product_name:
                button = product.find_element(*self.REMOVE_BUTTON)
                button.click()
                return True
        return False

    def get_cart_badge_count(self):
        """Get number of items in cart badge"""
        try:
            badge = self.find(self.CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def click_cart(self):
        """Click on cart icon"""
        self.click(self.CART_LINK)

    def get_all_product_names(self):
        """Get list of all product names"""
        products = self.get_all_products()
        names = []
        for product in products:
            name = product.find_element(*self.PRODUCT_NAME).text
            names.append(name)
        return names

    def get_all_product_prices(self):
        """Get list of all product prices as floats"""
        products = self.get_all_products()
        prices = []
        for product in products:
            price_text = product.find_element(*self.PRODUCT_PRICE).text
            price = float(price_text.replace("$", ""))
            prices.append(price)
        return prices

    def sort_by(self, option):
        """Sort products by option (e.g., 'az', 'za', 'lohi', 'hilo')"""
        dropdown = self.find(self.SORT_DROPDOWN)
        dropdown.find_element(By.TAG_NAME, "select").send_keys(option)
