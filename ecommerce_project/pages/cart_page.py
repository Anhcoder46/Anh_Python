from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")

    def get_cart_items(self):
        return self.find_all(self.CART_ITEMS)

    def is_cart_empty(self):
        try:
            items = self.get_cart_items()
            return len(items) == 0
        except:
            return True

    def get_item_count(self):
        try:
            items = self.get_cart_items()
            return len(items)
        except:
            return 0

    def remove_item(self, item_index=0):
        items = self.get_cart_items()
        remove_button = items[item_index].find_element(*self.REMOVE_BUTTON)
        remove_button.click()

    def remove_item_by_name(self, item_name):
        """Remove item from cart by name"""
        items = self.get_cart_items()
        for item in items:
            name = item.find_element(*self.CART_ITEM_NAME).text
            if name == item_name:
                button = item.find_element(*self.REMOVE_BUTTON)
                button.click()
                return True
        return False

    def get_cart_item_names(self):
        items = self.get_cart_items()
        names = []
        for item in items:
            name = item.find_element(*self.CART_ITEM_NAME).text
            names.append(name)
        return names

    def get_cart_total_price(self):
        # This locator may need adjustment based on actual DOM
        try:
            total = self.find((By.CLASS_NAME, "summary_total_label"))
            price_text = total.text.split("$")[-1]
            return float(price_text)
        except:
            return 0.0

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
