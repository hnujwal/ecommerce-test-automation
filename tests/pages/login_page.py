from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, ".title")
    
    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()