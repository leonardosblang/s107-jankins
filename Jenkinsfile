pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python setup.py build'
                archiveArtifacts 'dist/*.exe'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                    python -m unittest
                   '''
                   archiveArtifacts 'test/unit-test.xml'
            }
        }
        stage('Notification') {
            steps {
                echo 'Sending email....'
                sh '''
                    cd scripts/
                    chmod 775 *
                    ./scripts/shell.sh
                   '''
            }
        }
    }
}
