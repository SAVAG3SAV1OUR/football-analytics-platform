from src.api.client import get_data
from src.utils.logger import setup_logging
from src.utils.file_handler import save_raw_seasons, load_raw_seasons
import logging


setup_logging()
logger = logging.getLogger(__name__)

"""=============Get information about a specific season from a specific competition==========================="""
def get_season_details(comp_id,season_id,comp_name):
    endpoint = f"tournament/{comp_id}/season/{season_id}/info"

    cached_season = load_raw_seasons(comp_id,comp_name, season_id)

    if cached_season is not None:
        logger.info(f"Using cached data for season {season_id} from {comp_name} ({comp_id})")
        return cached_season

    details = get_data(endpoint)
    season_path = save_raw_seasons(comp_id,comp_name,season_id,details)
    logger.info(f"Saved season {season_id} from {comp_name} to {season_path}")

    return details

