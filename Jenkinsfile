pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-flask-app'
        DOCKER_REGISTRY = 'my-dockerhub-repo/my-flask-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run('-d -p 8777:8777 -v $PWD/Scores.txt:/app/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def testStatus = sh(script: 'docker exec my-flask-app python e2e.py', returnStatus: true)
                    if (testStatus != 0) {
                        error "Tests failed"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).stop()
                    docker.image(DOCKER_IMAGE).rm()
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image(DOCKER_REGISTRY).push('latest')
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                try {
                    docker.image(DOCKER_IMAGE).stop()
                    docker.image(DOCKER_IMAGE).rm()
                } catch (Exception e) {
                    echo "Error stopping/removing container: ${e.message}"
                }
            }
        }
    }
}
