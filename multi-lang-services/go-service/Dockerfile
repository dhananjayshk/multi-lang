# Use a Go base image
FROM golang:1.17-alpine

# Set the working directory
WORKDIR /app

# Copy Go modules and install dependencies
COPY go.mod go.sum ./
RUN go mod tidy

# Copy the rest of the application code
COPY . .

# Build the Go application
RUN go build -o go-service .

# Expose the port the app will run on
EXPOSE 8080

# Command to run the app
CMD ["./go-service"]

