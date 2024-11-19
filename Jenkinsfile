pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                dir('lab11') { // Работать только с папкой lab11
                    sh 'python3 --version'
                    sh 'pip3 install --upgrade pip'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                dir('lab11') { // Работать только с папкой lab11
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                dir('lab11') { // Работать только с папкой lab11
                    sh 'pytest'
                }
            }
        }
    }

    post {
        always {
            dir('lab11') { // Результаты из lab11
                junit 'report.xml'
            }
        }
    }
}
