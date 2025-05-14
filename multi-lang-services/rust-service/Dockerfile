# 1. Use official Rust image
FROM rust:1.75 as builder

# 2. Create app directory
WORKDIR /usr/src/app

# 3. Copy manifest and source files
COPY . .

# 4. Build your project
RUN cargo build --release

# 5. Create minimal final image (optional)
FROM debian:buster-slim
WORKDIR /app
COPY --from=builder /usr/src/app/target/release/rust-service .
CMD ["./rust-service"]

