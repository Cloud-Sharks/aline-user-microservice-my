pipeline{

    agent any

    environment{
        //set env vars
        AWS_ID = credentials('AWS_ID')
        SERVICE_NAME = 'user-ms'
        REGION = '${env.AWS_REGION}' 
        APP_NAME = 'my-user-microservice'
        APP_ENV = '${env.APP_ENV}'
        ORGANIZATION = 'Aline-Financial-MY'
        PROJECT_NAME = 'aline-user-microservice-my'
    }

    stages{
        stage('Checkout'){
            steps{
                //get branch
                git branch: 'dev', url: 'https://github.com/markyates7748/aline-user-microservice-my.git'
                sh'git submodule init'
                sh'git submodule update'
                script{
                    env.COMMIT_HASH=sh'${GIT_COMMIT:0:9}'
                }
            }
        }
        stage('Test'){
            steps{
                //run project tests
                sh'mvn clean test'
            }
        }
        stage('Package'){
            steps{
                //package project
                sh'mvn package -DskipTests'
            }
        }
        stage('Build Image'){
            steps{
                //build docker image
                sh'docker build . -t ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH}'
                sh'docker tag ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH} ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
                sh'docker tag ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH} ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:latest'
            }
        }
        stage('Push Image'){
            steps{
                //push image to cloud
                sh'aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $AWS_ID.dkr.ecr.$REGION.amazonaws.com'
                sh'docker push ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
                sh'docker push ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:latest'
            }
        }
        //deploy stage
    }

    post{
        always{
            //clean up
            sh'mvn clean'
            sh'docker image prune -a -f'
        }
    }

}
