from base.base_test import BaseTest

class TestLogin(BaseTest):
    def test_page_loads(self):
        self.driver.get(self.config['base_url'])
        assert "Example" in self.driver.title