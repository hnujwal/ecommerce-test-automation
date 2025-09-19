pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image with Python environment...'
                script {
                    bat 'docker build -t ecommerce-tests .'
                }
            }
        }
        
        stage('Run Tests in Docker') {
            steps {
                echo 'Running all tests in Docker container...'
                script {
                    bat '''
                        docker run --rm -v "%cd%\tests\reports:/app/tests/reports" ecommerce-tests
                    '''
                }
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
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            script {
                bat 'docker rmi ecommerce-tests || exit 0'
            }
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