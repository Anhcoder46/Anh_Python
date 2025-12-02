from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object for Checkout page"""

    # Locators - Step 1
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # Locators - Overview
    OVERVIEW_ITEM = (By.CLASS_NAME, "cart_item")
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_TOTAL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    # Locators - Confirmation
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        """Enter first name"""
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        """Enter last name"""
        self.type(self.LAST_NAME_INPUT, last_name)

    def enter_zip_code(self, zip_code):
        """Enter zip/postal code"""
        self.type(self.ZIP_CODE_INPUT, zip_code)

    def fill_checkout_info(self, first_name, last_name, zip_code):
        """Fill all checkout information"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)

    def click_continue(self):
        """Click continue button"""
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        """Click finish button"""
        self.click(self.FINISH_BUTTON)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Check if error message is displayed"""
        try:
            self.find(self.ERROR_MESSAGE)
            return True
        except:
            return False

    def get_overview_items(self):
        """Get all items in overview page"""
        return self.find_all(self.OVERVIEW_ITEM)

    def is_item_in_overview(self, item_name):
        """Check if specific item is in overview"""
        items = self.get_overview_items()
        for item in items:
            try:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                if name == item_name:
                    return True
            except:
                pass
        return False

    def get_confirmation_message(self):
        """Get order confirmation message"""
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def is_order_complete(self):
        """Check if order is completed successfully"""
        try:
            message = self.get_confirmation_message()
            return "thank you" in message.lower()
        except:
            return False
