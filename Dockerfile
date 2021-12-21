FROM openjdk:8-jdk-alpine
COPY ./user-microservice/target/user-microservice-0.1.0.jar app.jar
# ENV DB_HOST localhost
# ENV DB_NAME alinedb
# ENV DB_PASSWORD pwd
# ENV DB_PORT 3306
# ENV DB_USERNAME user
# ENV ENCRYPT_SECRET_KEY NVNCWq4KEDHXNjsazdGX2oZ1
# ENV JWT_SECRET_KEY 1wHqQFdUlUr5TZNr1wTCiuyM0Vye2L4jX
# EXPOSE 8070
ENTRYPOINT ["java", "-jar", "/app.jar"]