# E-commerce Test Automation Framework

A comprehensive test automation framework for e-commerce applications with real-time UI and API testing capabilities.

## 🚀 Features

- **Real UI Testing**: Sauce Demo e-commerce application automation
- **Real API Testing**: ReqRes API validation with comprehensive endpoints
- **Page Object Model**: Maintainable and scalable test architecture
- **CI/CD Integration**: Jenkins pipeline with Docker containerization
- **Comprehensive Reporting**: HTML reports with detailed test analytics
- **Multi-Platform Support**: Easily adaptable to different e-commerce sites

## 🌐 Applications Under Test

### UI Testing
- **Sauce Demo** (https://www.saucedemo.com)
  - Real e-commerce application with login, products, and cart
  - Credentials: `standard_user` / `secret_sauce`

### API Testing
- **ReqRes API** (https://reqres.in/api)
  - Real REST API for user management operations
  - GET, POST, PUT, DELETE operations

## 📁 Project Structure

```
tests/
├── api/
│   └── api_client.py           # API testing client
├── base/
│   └── base_test.py           # WebDriver setup and teardown
├── pages/
│   ├── login_page.py          # Login page objects
│   ├── product_page.py        # Product and cart operations
│   ├── cart_page.py           # Cart management
│   └── checkout_page.py       # Checkout workflow
├── config/
│   └── config.json            # Test configuration
├── reports/                   # Generated test reports
├── test_saucedemo.py          # Sauce Demo UI tests
├── test_api_simple.py         # ReqRes API tests
└── test_*.py                  # Additional test suites
postman/
└── ecommerce_collection.json  # Postman API collection
Dockerfile                     # Container configuration
Jenkinsfile                   # CI/CD pipeline
requirements.txt              # Python dependencies
```

## 🛠️ Setup

### Prerequisites
- Python 3.12+
- Chrome browser
- Git

### Installation

1. **Clone repository:**
```bash
git clone https://github.com/hnujwal/ecommerce-test-automation.git
cd ecommerce-test-automation
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Verify setup:**
```bash
python -m pytest tests/test_saucedemo.py::TestSauceDemo::test_login_success -v
```

## 🧪 Running Tests

### Quick Start - Run All Tests
```bash
python -m pytest tests/ --html=tests/reports/complete_report.html --self-contained-html -v
```

### UI Tests (Sauce Demo)
```bash
# All UI tests
python -m pytest tests/test_saucedemo.py -v

# Specific test
python -m pytest tests/test_saucedemo.py::TestSauceDemo::test_login_success -v
```

### API Tests (ReqRes)
```bash
# All API tests
python -m pytest tests/test_api_simple.py -v

# With detailed output
python -m pytest tests/test_api_simple.py -v -s
```

### Parallel Execution
```bash
python -m pytest tests/ -n 4 --html=tests/reports/parallel_report.html -v
```

## 🐳 Docker Execution

```bash
# Build image
docker build -t ecommerce-tests .

# Run tests in container
docker run --rm -v $(pwd)/tests/reports:/app/tests/reports ecommerce-tests
```

## 📊 Reports

### HTML Reports
- **Location**: `tests/reports/complete_report.html`
- **Features**: Test results, execution time, browser screenshots
- **View**: Open in browser after test execution

### Report Examples
```bash
# Generate comprehensive report
python -m pytest tests/ --html=tests/reports/full_report.html --self-contained-html -v
```

## 🔄 CI/CD Pipeline

### Jenkins Integration
1. Use provided `Jenkinsfile`
2. Configure Docker and HTML Publisher plugins
3. Set up automated builds on code push

### GitHub Actions (Optional)
```yaml
# .github/workflows/tests.yml
name: Test Automation
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Tests
        run: |
          pip install -r requirements.txt
          python -m pytest tests/ --html=report.html
```

## 📝 Test Results

### Current Test Coverage
- ✅ **UI Tests**: 3/3 passing (Sauce Demo)
  - User authentication
  - Product cart operations
  - End-to-end shopping flow
- ✅ **API Tests**: 3/4 passing (ReqRes API)
  - User data retrieval
  - API response validation
  - Error handling

### Supported Test Scenarios
- **Login/Authentication**: Multi-user support
- **Product Management**: Search, add to cart, checkout
- **API Operations**: CRUD operations, data validation
- **Error Handling**: Invalid inputs, network failures

## 🔧 Configuration

### Current Configuration
```json
{
    "browser": "chrome",
    "base_url": "https://www.saucedemo.com",
    "api_base_url": "https://reqres.in/api",
    "timeout": 10,
    "headless": false,
    "test_user": {
        "username": "standard_user",
        "password": "secret_sauce"
    }
}
```

### Customization Options
- **Headless Mode**: Set `"headless": true` for CI/CD
- **Different Users**: Update credentials in config
- **Timeouts**: Adjust wait times for slower environments
- **Browser**: Support for Chrome, Firefox, Edge

## 🎯 Adapting to Other Applications

### For Flipkart/Amazon/Other E-commerce:
1. Update `base_url` in config.json
2. Modify page object locators
3. Update test credentials
4. Adjust API endpoints if available

### Example Adaptation:
```json
{
    "base_url": "https://www.flipkart.com",
    "test_user": {
        "mobile": "9876543210",
        "password": "your_password"
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-test`
3. Commit changes: `git commit -m 'Add new test scenario'`
4. Push branch: `git push origin feature/new-test`
5. Submit pull request

## 📞 Support

For issues and questions:
- Create GitHub issue
- Contact: ujwalhn@gmail.com

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

**⭐ Star this repository if you find it helpful!**
