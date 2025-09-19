pipeline {
    agent any
    
    environment {
        PYTHON_PATH = '/usr/bin/python3'
        CHROME_BIN = '/usr/bin/google-chrome'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run UI Tests') {
            steps {
                echo 'Running Sauce Demo UI tests...'
                sh '''
                    . venv/bin/activate
                    python -m pytest tests/test_saucedemo.py -v --html=tests/reports/ui_report.html --self-contained-html
                '''
            }
        }
        
        stage('Run API Tests') {
            steps {
                echo 'Running ReqRes API tests...'
                sh '''
                    . venv/bin/activate
                    python -m pytest tests/test_api_simple.py -v --html=tests/reports/api_report.html --self-contained-html
                '''
            }
        }
        
        stage('Run All Tests') {
            steps {
                echo 'Running complete test suite...'
                sh '''
                    . venv/bin/activate
                    python -m pytest tests/ -v --html=tests/reports/complete_report.html --self-contained-html
                '''
            }
        }
        
        stage('Publish Reports') {
            steps {
                echo 'Publishing HTML test reports...'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'tests/reports',
                    reportFiles: 'complete_report.html',
                    reportName: 'Complete Test Report'
                ])
                
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'tests/reports',
                    reportFiles: 'ui_report.html',
                    reportName: 'UI Test Report'
                ])
                
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'tests/reports',
                    reportFiles: 'api_report.html',
                    reportName: 'API Test Report'
                ])
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
    }
}