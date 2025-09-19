# E-commerce Test Automation Framework

A comprehensive test automation framework for e-commerce applications covering UI, API, and CI/CD integration.

## 🚀 Features

- **UI Testing**: Login, product search, cart, and checkout workflows
- **API Testing**: REST API validation with Python and Postman/Newman
- **CI/CD Integration**: Jenkins pipeline with Docker containerization
- **Reporting**: HTML and Allure reports with detailed analytics
- **Page Object Model**: Maintainable and scalable test architecture

## 📁 Project Structure

```
tests/
├── api/
│   └── api_client.py           # API testing client
├── base/
│   └── base_test.py           # WebDriver setup and teardown
├── pages/
│   ├── login_page.py          # Login page objects
│   ├── product_page.py        # Product search and cart
│   ├── cart_page.py           # Cart operations
│   └── checkout_page.py       # Checkout workflow
├── config/
│   └── config.json            # Test configuration
├── reports/                   # Generated test reports
├── test_ecommerce_ui.py       # UI test scenarios
└── test_api.py               # API test cases
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
- Docker (optional)
- Jenkins (for CI/CD)

### Installation

1. **Clone and setup environment:**
```bash
git clone <repository-url>
cd ecommerce-test-framework
pip install -r requirements.txt
```

2. **Configure test settings:**
Edit `tests/config/config.json`:
```json
{
    "browser": "chrome",
    "base_url": "https://demo.opencart.com",
    "api_base_url": "https://demo.opencart.com/api",
    "timeout": 10,
    "headless": false
}
```

## 🧪 Running Tests

### UI Tests
```bash
# All UI tests
python -m pytest tests/test_ecommerce_ui.py

# Specific test
python -m pytest tests/test_ecommerce_ui.py::TestEcommerceUI::test_login_workflow
```

### API Tests
```bash
# All API tests
python -m pytest tests/test_api.py

# With verbose output
python -m pytest tests/test_api.py -v
```

### All Tests with Reports
```bash
# HTML + Allure reports
python -m pytest tests/ --html=tests/reports/report.html --alluredir=allure-results

# Parallel execution
python -m pytest tests/ -n 4
```

### Postman/Newman Tests
```bash
# Install Newman
npm install -g newman

# Run collection
newman run postman/ecommerce_collection.json --reporters html,json
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
- Location: `tests/reports/report.html`
- Features: Test results, screenshots, execution time

### Allure Reports
```bash
# Generate Allure report
allure serve allure-results

# Generate static report
allure generate allure-results --clean
```

## 🔄 CI/CD Pipeline

### Jenkins Setup
1. Install required plugins: Docker, HTML Publisher, Allure
2. Create pipeline job using `Jenkinsfile`
3. Configure webhook for automatic builds

### Pipeline Stages
- **Checkout**: Pull latest code
- **Build**: Create Docker image
- **Test**: Execute test suites
- **Report**: Generate and publish reports

## 📝 Test Scenarios

### UI Test Coverage
- ✅ User login workflow
- ✅ Product search and selection
- ✅ Add products to cart
- ✅ Cart management
- ✅ Checkout process

### API Test Coverage
- ✅ Product catalog API
- ✅ Cart operations API
- ✅ User authentication API
- ✅ Order management API

## 🔧 Configuration

### Browser Settings
```json
{
    "browser": "chrome|firefox|edge",
    "headless": true|false,
    "timeout": 10
}
```

### Environment Variables
```bash
export TEST_ENV=staging
export BROWSER=chrome
export HEADLESS=true
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
- Contact: test-automation-team@company.com

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.