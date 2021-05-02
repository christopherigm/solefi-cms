pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Copy') {
            environment {
                PUBLIC_URL = ''
            }
            steps {
                sh 'rm -rf /var/www/apps/staging/solefi-cms'
                sh 'mkdir /var/www/apps/staging/solefi-cms'
                sh 'cp -r ./* /var/www/apps/staging/solefi-cms'
            }
        }
        stage('Build') {
            steps {
                sh 'source /home/christopher/.virtualenvs/solefi/bin/activate'
                dir('/var/www/apps/staging/solefi-cms') {
                    sh 'python3 -m pip freeze -l > req.txt'
                }
            }
        }
    }
}