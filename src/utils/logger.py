import logging
import os
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = Path(LOG_DIR/"pipeline.log")

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
