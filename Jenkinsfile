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
            steps {
                sh '. /home/christopher/.virtualenvs/solefi/bin/activate'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
    }
}