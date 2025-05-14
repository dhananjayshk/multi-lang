import socket
import logging
import json
from pythonjsonlogger import jsonlogger

class LogstashTCPHandler(logging.Handler):
    def __init__(self, host, port):
        super().__init__()
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
        except Exception as e:
            print(f"[WARNING] Could not connect to Logstash: {e}")
            self.sock = None

    def emit(self, record):
        if not self.sock:
            return
        try:
            msg = self.format(record)
            self.sock.sendall((msg + "\n").encode("utf-8"))
        except Exception:
            self.handleError(record)

def setup_logger(logstash_host="localhost", logstash_port=5044):
    logger = logging.getLogger("fastapi-app")
    logger.setLevel(logging.INFO)

    formatter = jsonlogger.JsonFormatter(
        fmt='%(asctime)s %(levelname)s %(message)s',
        rename_fields={"levelname": "severity", "asctime": "timestamp"}
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    try:
        logstash_handler = LogstashTCPHandler(logstash_host, logstash_port)
        logstash_handler.setFormatter(formatter)
        logger.addHandler(logstash_handler)
    except Exception as e:
        print(f"[WARNING] Failed to initialize Logstash handler: {e}")

    return logger
