pipeline{

    agent any

    environment{
        //set env vars
        AWS_ID = credentials('AWS_ID')
        APP_NAME = 'my-user-microservice'
    }

    stages{
        stage('Checkout'){
            steps{
                //get branch
                checkout([$class: 'GitSCM', 
                    branches: [[name: env.BRANCH_MY]]])
                sh'git submodule init'
                sh'git submodule update'
            }
        }
        stage('Test'){
            steps{
                //run test cases
                sh'mvn clean test'
            }
        }
        stage('SonarQube Analysis'){
            steps{
                //scan with SonarQube
                withSonarQubeEnv('SonarQubeServer'){
                    sh'mvn clean verify sonar:sonar'
                }
            }
        }
        stage('QualityGate'){
            steps{
                //wait for quality response
                timeout(time: 10, unit: 'MINUTES'){
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage('Package'){
            steps{
                //package project
                sh'mvn package -DskipTests'
            }
        }
        stage('Build Image'){
            environment{
                COMMIT_HASH = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            }
            steps{
                //build docker image
                sh'docker build . -t ${AWS_ID}.dkr.ecr.${ECR_REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
                sh'docker tag ${AWS_ID}.dkr.ecr.${ECR_REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH} ${AWS_ID}.dkr.ecr.${ECR_REGION}.amazonaws.com/${APP_NAME}:latest'
            }
        }
        stage('Push Image'){
            environment{
                COMMIT_HASH = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            }
            steps{
                //push image to cloud
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "cloudshark-Mark", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]){
                    sh'aws ecr get-login-password --region $ECR_REGION | docker login --username AWS --password-stdin $AWS_ID.dkr.ecr.$ECR_REGION.amazonaws.com'
                    sh'docker push ${AWS_ID}.dkr.ecr.${ECR_REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
                    sh'docker push ${AWS_ID}.dkr.ecr.${ECR_REGION}.amazonaws.com/${APP_NAME}:latest'
                }
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
