import requests
import os
import time
from dotenv import load_dotenv
from src.utils.logger import setup_logging
import logging

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

API_KEY = os.getenv("API_KEY")
HEADERS = {'x-api-key': API_KEY}
BASE_URL = os.getenv("BASE_URL")

MAX_RETRIES = 3
RETRY_DELAY = 2


def get_data(url):

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info("Requesting endpoint...")
            response = requests.get(
                f"{BASE_URL}/{url}", 
                headers=HEADERS,
                timeout=30
            )

            response.raise_for_status()

            logger.info(f"Successfully retrieved data from : {url}")

            return response.json()
        except requests.RequestException as e:
            logger.warning(
                f"Request failed for {url}, "
                f"(attempt {attempt}/{MAX_RETRIES}): {e}"
            )

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(
                    f"Failed to retrieve data forom {url} "
                    f"after {MAX_RETRIES} attempts"
                )

                raise





