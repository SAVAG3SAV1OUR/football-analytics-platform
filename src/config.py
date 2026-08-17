from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
RAW_COMPS_DIR = RAW_DATA_DIR / "competitions"
DISCOVERY_DIR = RAW_DATA_DIR / "discovery"

RAW_COMPS_DIR.mkdir(parents=True, exist_ok=True)
DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)
