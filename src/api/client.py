import requests
import os
from dotenv import load_dotenv
from utils.logger import setup_logging
import logging

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

API_KEY = os.getenv("API_KEY")
HEADERS = {'x-api-key': API_KEY}
BASE_URL = os.getenv("BASE_URL")


def get_data(url):
    logger.info("Requesting endpoint...")

    response = requests.get(
        f"{BASE_URL}/{url}", 
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()
    logger.info(f"Successfully retrieved data from : {url}")

    return response.json()