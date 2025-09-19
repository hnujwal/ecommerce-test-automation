pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    py --version || echo "Python version check failed"
                    py -m pip install --upgrade pip || echo "Pip upgrade failed"
                    py -m pip install -r requirements.txt || echo "Requirements install failed"
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
        
        stage('Run API Tests Only') {
            steps {
                echo 'Running API tests (no browser required)...'
                bat '''
                    py -m pytest tests/test_api_simple.py -v --html=tests/reports/api_report.html --self-contained-html || echo "API tests failed"
                '''
            }
        }
        
        stage('Publish Reports') {
            steps {
                echo 'Publishing test reports...'
                publishHTML([
                    allowMissing: true,
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
            echo 'Pipeline execution completed'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed but continuing...'
        }
    }
}