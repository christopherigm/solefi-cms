pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            environment {
                PY_WRAPPER = '/home/christopher/.virtualenvs/solefi/bin/python3'
            }
            steps {
                sh '. /home/christopher/.virtualenvs/solefi/bin/activate'
                sh '$PY_WRAPPER -m pip install -r requirements.txt'
                sh '$PY_WRAPPER manage.py migrate'
                sh '$PY_WRAPPER manage.py collectstatic --noinput'
            }
        }
        stage('Deploy') {
            environment {
                MEDIA_DIR = '/var/www/apps/staging/solefi-cms/media'
            }
            if(fileExists('media')) {
                sh 'rm -rf media'
            }
            if(fileExists('$MEDIA_DIR')) {
                sh 'cp -r $MEDIA_DIR ./'
            }
            steps {
                sh 'rm -rf /var/www/apps/staging/solefi-cms'
                sh 'mkdir /var/www/apps/staging/solefi-cms'
                sh 'cp -r ./* /var/www/apps/staging/solefi-cms'
            }
        }
        stage('Restart Supervisor') {
            steps {
                sh 'sudo supervisorctl reread'
                sh 'sudo supervisorctl update'
            }
        }
    }
}