pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        MEDIA_DIR = '/var/www/apps/staging/solefi-cms/media'
        LOCAL_MEDIA_EXIST = fileExists 'media'
        REMOTE_MEDIA_EXIST = fileExists '$MEDIA_DIR'
    }
    stages {
        stage('Build') {
            environment {
                PY_WRAPPER = '/home/christopher/.virtualenvs/solefi/bin/python3'
                env = 'staging'
                db_name = sh(script: 'echo $SOLEFI_STAGING_DB', , returnStdout: true).trim()
                db_user = sh(script: 'echo $SOLEFI_STAGING_DB', , returnStdout: true).trim()
                db_password = sh(script: 'echo $SOLEFI_STAGING_DB', , returnStdout: true).trim()
                email_id = 'john@doe.com'
                email_password = 'password'
            }
            steps {
                sh '. /home/christopher/.virtualenvs/solefi/bin/activate'
                sh '$PY_WRAPPER -m pip install -r requirements.txt'
                sh '$PY_WRAPPER manage.py migrate'
                sh '$PY_WRAPPER manage.py collectstatic --noinput'
            }
        }
        stage('Remove cached media') {
            when { expression { LOCAL_MEDIA_EXIST == 'true' } }
            steps {
                sh 'sudo rm -rf media'
            }
        }
        stage('Copy remote media') {
            when { expression { REMOTE_MEDIA_EXIST == 'true' } }
            steps {
                sh 'sudo cp -r $MEDIA_DIR ./'
                sh 'sudo chmod -R 777 $MEDIA_DIR'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo rm -rf /var/www/apps/staging/solefi-cms'
                sh 'sudo mkdir /var/www/apps/staging/solefi-cms'
                sh 'sudo cp -r ./* /var/www/apps/staging/solefi-cms'
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