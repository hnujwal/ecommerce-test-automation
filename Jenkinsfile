pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                    python.exe -m pip install --upgrade pip
                    python.exe -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Create Reports Directory') {
            steps {
                echo 'Creating reports directory...'
                bat '''
                    if not exist "tests\\reports" mkdir "tests\\reports"
                '''
            }
        }
        
        stage('Run UI Tests') {
            steps {
                echo 'Running Sauce Demo UI tests...'
                bat '''
                    python.exe -m pytest tests/test_saucedemo.py -v --html=tests/reports/ui_report.html --self-contained-html
                '''
            }
        }
        
        stage('Run API Tests') {
            steps {
                echo 'Running ReqRes API tests...'
                bat '''
                    python.exe -m pytest tests/test_api_simple.py -v --html=tests/reports/api_report.html --self-contained-html
                '''
            }
        }
        
        stage('Run All Tests') {
            steps {
                echo 'Running complete test suite...'
                bat '''
                    python.exe -m pytest tests/ -v --html=tests/reports/complete_report.html --self-contained-html
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
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}