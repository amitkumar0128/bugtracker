@Library("Shared") _
pipeline {
    agent any
    stages {
        stage ("Code") {
            steps {
                script {
                    clone("https://github.com/amitkumar0128/bugtracker.git","main")
                }
            }
        }
        stage ("Build and Depoly") {
            steps {
                script {
                    docker_deploy()
                }
            }
        }
    }
}