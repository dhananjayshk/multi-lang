pipeline {
    agent any

    environment {
        // Define environment variables if needed
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git
                git branch: 'main', url: 'https://github.com/dhananjayshk/multi-lang.git'
            }
        }

        stage('Build Services') {
            parallel {
                stage('Build Go Service') {
                    steps {
                        dir('go-service') {
                            sh 'docker build -t go-service:latest .'
                        }
                    }
                }
                stage('Build Java Service') {
                    steps {
                        dir('java-service') {
                            sh 'docker build -t java-service:latest .'
                        }
                    }
                }
                stage('Build Python Service') {
                    steps {
                        dir('python-service') {
                            sh 'docker build -t python-service:latest .'
                        }
                    }
                }
                stage('Build Rust Service') {
                    steps {
                        dir('rust-service') {
                            sh 'docker build -t rust-service:latest .'
                        }
                    }
                }
            }
        }

        stage('Deploy Services') {
            steps {
                // Bring up the services
                sh 'docker-compose up -d'
            }
        }

        stage('Integration Tests') {
            steps {
                // Run integration tests if applicable
                sh 'docker-compose run test-service'
            }
        }

        stage('Cleanup') {
            steps {
                // Remove unused containers and images
                sh 'docker system prune -f'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
            // Optionally, send notifications or trigger alerts
        }
    }
}
