from pathlib import Path
from dotenv import load_dotenv
import os

#File Directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
SILVER_DATA_DIR = DATA_DIR / "silver"
RAW_COMPS_DIR = RAW_DATA_DIR / "competitions"
DISCOVERY_DIR = RAW_DATA_DIR / "discovery"

RAW_COMPS_DIR.mkdir(parents=True, exist_ok=True)
DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)
SILVER_DATA_DIR.mkdir(parents=True, exist_ok=True)

#DB Connection (Postgres)
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
