FROM openjdk:8-jdk-alpine
COPY ./user-microservice/target/user-microservice-0.1.0.jar app.jar
ENV APP_PORT 8070
ENTRYPOINT ["java", "-jar", "/app.jar"]