import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        with open('tests/config/config.json') as f:
            self.config = json.load(f)
        
        options = webdriver.ChromeOptions()
        if self.config['headless']:
            options.add_argument('--headless')
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.implicitly_wait(self.config['timeout'])
        yield
        self.driver.quit()