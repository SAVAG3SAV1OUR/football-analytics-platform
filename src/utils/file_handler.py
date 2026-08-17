import json
from src.config import RAW_COMPS_DIR, DISCOVERY_DIR

def save_raw_comps(comp_id, data):
    file_path = RAW_COMPS_DIR / f"{comp_id}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return file_path

def load_raw_comps(comp_id):
    file_path = RAW_COMPS_DIR / f"{comp_id}.json"

    if not file_path.exists():
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_league_data(data):
    file_path = DISCOVERY_DIR / "leagues.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return file_path

def load_league_data():
    file_path = DISCOVERY_DIR / "leagues.json"

    if not file_path.exists():
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)