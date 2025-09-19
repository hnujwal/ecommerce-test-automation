from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    PRODUCT_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    
    def add_first_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()
    
    def get_cart_count(self):
        try:
            return self.driver.find_element(*self.CART_BADGE).text
        except:
            return "0"
    
    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()