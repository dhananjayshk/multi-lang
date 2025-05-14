from fastapi import FastAPI
from log_handler import setup_logger
import uvicorn

# Setup logger
logger = setup_logger(logstash_host="localhost", logstash_port=5044)

app = FastAPI()

@app.get("/")
async def root():
    logger.info("Received GET request on /")
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
