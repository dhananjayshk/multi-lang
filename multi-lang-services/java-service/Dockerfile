# ---- Stage 1: Build the application ----
FROM maven:3.8.6-eclipse-temurin-17 AS builder

WORKDIR /usr/src/app

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests

# ---- Stage 2: Run the application ----
FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

COPY --from=builder /usr/src/app/target/java-service-1.0-SNAPSHOT.jar app.jar

CMD ["java", "-jar", "app.jar"]

