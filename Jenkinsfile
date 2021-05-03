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
                email_id = 'john@doe.com'
                email_password = 'password'
            }
            steps {
                sh 'export db_name=$SOLEFI_STAGING_DB'
                sh 'export db_user=$SOLEFI_STAGING_DB'
                sh 'export db_password=$SOLEFI_STAGING_DB'
                sh '. /home/christopher/.virtualenvs/solefi/bin/activate'
                sh '$PY_WRAPPER -m pip install -r requirements.txt'
                sh '$PY_WRAPPER manage.py migrate'
                sh '$PY_WRAPPER manage.py collectstatic --noinput'
            }
        }
        stage('Remove cached media') {
            when { expression { LOCAL_MEDIA_EXIST == 'true' } }
            steps {
                sh 'rm -rf media'
            }
        }
        stage('Copy remote media') {
            when { expression { REMOTE_MEDIA_EXIST == 'true' } }
            steps {
                sh 'cp -r $MEDIA_DIR ./'
            }
        }
        stage('Deploy') {
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