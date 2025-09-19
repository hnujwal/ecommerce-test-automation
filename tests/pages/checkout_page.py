from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    GUEST_CHECKOUT = (By.CSS_SELECTOR, "input[value='guest']")
    CONTINUE_BUTTON = (By.ID, "button-account")
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    EMAIL = (By.ID, "input-payment-email")
    
    def select_guest_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.GUEST_CHECKOUT)).click()
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
    
    def fill_billing_details(self, first_name, last_name, email):
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)