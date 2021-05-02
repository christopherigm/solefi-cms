pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Copy') {
            steps {
                sh 'rm -rf /var/www/apps/staging/solefi-cms'
                sh 'mkdir /var/www/apps/staging/solefi-cms'
                sh 'cp -r ./* /var/www/apps/staging/solefi-cms'
            }
        }
        stage('Build') {
            environment {
                PY_WRAPPER = '/opt/venv/solefi/bin/python3'
            }
            steps {
                dir('/var/www/apps/staging/solefi-cms') {
                    sh '$PY_WRAPPER -m pip install -r requirements.txt'
                }
            }
        }
    }
}