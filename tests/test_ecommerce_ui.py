from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

class TestEcommerceUI(BaseTest):
    
    def test_login_workflow(self):
        self.driver.get(self.config['base_url'])
        login_page = LoginPage(self.driver)
        # Basic login test - adapt to actual site structure
        assert "OpenCart" in self.driver.title
    
    def test_product_search_and_add_to_cart(self):
        self.driver.get(self.config['base_url'])
        product_page = ProductPage(self.driver)
        
        product_page.search_product("iPhone")
        product_page.select_first_product()
        product_page.add_to_cart()
        
        # Verify product added
        assert "cart" in self.driver.current_url.lower() or "success" in self.driver.page_source.lower()
    
    def test_cart_to_checkout_workflow(self):
        self.driver.get(self.config['base_url'])
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        # Add product to cart
        product_page.search_product("MacBook")
        product_page.select_first_product()
        product_page.add_to_cart()
        
        # View cart and checkout
        cart_page.view_cart()
        cart_page.proceed_to_checkout()
        
        # Fill checkout details
        checkout_page.select_guest_checkout()
        checkout_page.fill_billing_details("John", "Doe", "john@test.com")
        
        assert "checkout" in self.driver.current_url.lower()