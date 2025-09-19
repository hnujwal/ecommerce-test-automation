pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("ecommerce-tests:${env.BUILD_ID}")
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    docker.image("ecommerce-tests:${env.BUILD_ID}").inside {
                        sh 'python -m pytest tests/ --html=tests/reports/report.html --alluredir=allure-results'
                    }
                }
            }
        }
        
        stage('Generate Reports') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'tests/reports',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
                
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}