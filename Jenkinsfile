pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        APP_FOLDER = "solefi-api"
        BRANCH = sh(script: "echo ${BRANCH}", , returnStdout: true).trim()
    }
    stages {
        stage("Check App folders") {
            steps {
                sh "sudo mkdir /$APP_FOLDER -p"
                sh "sudo chmod -R 777 /$APP_FOLDER"

                sh "sudo mkdir /$APP_FOLDER/db -p"
                sh "sudo chmod -R 777 /$APP_FOLDER/db"

                sh "sudo mkdir /$APP_FOLDER/static -p"
                sh "sudo chmod -R 777 /$APP_FOLDER/static"

                sh "sudo mkdir /$APP_FOLDER/media -p"
                sh "sudo chmod -R 777 /$APP_FOLDER/media"
            }
        }
        stage("Deploy and start instance") {
            steps {
                sh "cp /$APP_FOLDER/env.default /$APP_FOLDER/env"
                sh "echo BRANCH=$BRANCH >> /$APP_FOLDER/env"
                sh "sudo docker-compose --env-file /$APP_FOLDER/env -f ./docker-compose.yaml pull"
                sh "sudo docker-compose --env-file /$APP_FOLDER/env -f ./docker-compose.yaml down --remove-orphans -f"
                sh "sudo docker-compose --env-file /$APP_FOLDER/env -f ./docker-compose.yaml up -d"
            }
        }
    }
}
