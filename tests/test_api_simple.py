import pytest
import json
from api.api_client import APIClient

class TestEcommerceAPISimple:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        with open('tests/config/config.json') as f:
            self.config = json.load(f)
        self.api_client = APIClient(self.config['api_base_url'])
    
    def test_get_users_list(self):
        """Test getting customer list - simulates user management"""
        response = self.api_client.get_users(page=1)
        assert response.status_code == 200
        data = response.json()
        assert 'data' in data
        assert len(data['data']) > 0
        print(f"Found {len(data['data'])} users")
    
    def test_get_single_customer(self):
        """Test getting single customer profile"""
        response = self.api_client.get_user(user_id=2)
        assert response.status_code == 200
        data = response.json()
        assert 'data' in data
        assert data['data']['id'] == 2
        print(f"Customer: {data['data']['first_name']} {data['data']['last_name']}")
    
    def test_customer_not_found(self):
        """Test handling non-existent customer"""
        response = self.api_client.get_user(user_id=23)  # Use ID that returns 404
        assert response.status_code == 404
        print("Correctly handled non-existent customer")
    
    def test_api_response_structure(self):
        """Test API response structure validation"""
        response = self.api_client.get_users(page=1)
        assert response.status_code == 200
        data = response.json()
        
        # Validate response structure
        required_fields = ['page', 'per_page', 'total', 'total_pages', 'data']
        for field in required_fields:
            assert field in data, f"Missing field: {field}"
        
        # Validate user data structure
        if data['data']:
            user = data['data'][0]
            user_fields = ['id', 'email', 'first_name', 'last_name', 'avatar']
            for field in user_fields:
                assert field in user, f"Missing user field: {field}"
        
        print("API response structure validated successfully")