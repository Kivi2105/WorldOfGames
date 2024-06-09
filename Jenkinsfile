pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('my-flask-app')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('my-flask-app').run('-p 8777:8777 -v $PWD/Scores.txt:/app/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def testStatus = sh(script: 'python e2e.py', returnStatus: true)
                    if (testStatus != 0) {
                        error "Tests failed"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    docker.image('my-flask-app').stop()
                    docker.image('my-flask-app').push('my-dockerhub-repo/my-flask-app')
                }
            }
        }
    }
}
