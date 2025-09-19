from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

class TestSauceDemo(BaseTest):
    
    def test_login_success(self):
        self.driver.get(self.config['base_url'])
        login_page = LoginPage(self.driver)
        
        login_page.enter_username(self.config['test_user']['username'])
        login_page.enter_password(self.config['test_user']['password'])
        login_page.click_login()
        
        # Verify successful login
        assert "inventory" in self.driver.current_url
        assert len(self.driver.find_elements(*login_page.PRODUCTS_TITLE)) > 0
    
    def test_add_product_to_cart(self):
        self.driver.get(self.config['base_url'])
        login_page = LoginPage(self.driver)
        product_page = ProductPage(self.driver)
        
        # Login first
        login_page.enter_username(self.config['test_user']['username'])
        login_page.enter_password(self.config['test_user']['password'])
        login_page.click_login()
        
        # Add product to cart
        product_page.add_first_product_to_cart()
        
        # Wait and verify cart count
        import time
        time.sleep(1)
        cart_count = product_page.get_cart_count()
        assert cart_count == "1"
    
    def test_complete_shopping_flow(self):
        self.driver.get(self.config['base_url'])
        login_page = LoginPage(self.driver)
        product_page = ProductPage(self.driver)
        
        # Login
        login_page.enter_username(self.config['test_user']['username'])
        login_page.enter_password(self.config['test_user']['password'])
        login_page.click_login()
        
        # Add product and go to cart
        product_page.add_first_product_to_cart()
        import time
        time.sleep(1)
        product_page.go_to_cart()
        
        # Verify cart page
        time.sleep(2)
        assert "cart" in self.driver.current_url or "Cart" in self.driver.page_source