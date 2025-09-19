import requests
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})
    
    def get_users(self, page=1):
        """Get users - simulates getting customer data"""
        response = self.session.get(f"{self.base_url}/users?page={page}")
        return response
    
    def get_user(self, user_id):
        """Get single user - simulates getting customer profile"""
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        return response
    
    def create_user(self, name, job):
        """Create user - simulates user registration"""
        payload = {"name": name, "job": job}
        response = self.session.post(f"{self.base_url}/users", json=payload)
        return response
    
    def update_user(self, user_id, name, job):
        """Update user - simulates profile update"""
        payload = {"name": name, "job": job}
        response = self.session.put(f"{self.base_url}/users/{user_id}", json=payload)
        return response
    
    def delete_user(self, user_id):
        """Delete user - simulates account deletion"""
        response = self.session.delete(f"{self.base_url}/users/{user_id}")
        return response
    
    def login_user(self, email, password):
        """User login - simulates authentication"""
        payload = {"email": email, "password": password}
        response = self.session.post(f"{self.base_url}/login", json=payload)
        return response
    
    def register_user(self, email, password):
        """User registration - simulates account creation"""
        payload = {"email": email, "password": password}
        response = self.session.post(f"{self.base_url}/register", json=payload)
        return response