from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    CART_BUTTON = (By.ID, "cart")
    VIEW_CART = (By.XPATH, "//a[contains(text(),'View Cart')]")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[name^='quantity']")
    
    def view_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.VIEW_CART)).click()
    
    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()