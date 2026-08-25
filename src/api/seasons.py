from src.api.client import get_data
from src.utils.logger import setup_logging
from src.utils.file_handler import save_raw_seasons, load_raw_seasons
import logging


setup_logging()
logger = logging.getLogger(__name__)

"""================Get all seasons from a competition====================================================="""
def discover_seasons(comp_id):
    seasons = []

    logger.info("==========================================================================")
    seasons_data = get_data(f"tournaments/{comp_id}/seasons")

    for season in seasons_data.get("seasons",[]):
        seasons.append({
            "season_id": season.get("id"),
            "season_name": season.get("name"),
            "season_year": season.get("year"),
            "comp_id": season.get("tournamentId")
        })

    return seasons


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


def collect_season_details(comp_id, comp_name, limit=None):
    seasons = discover_seasons(comp_id)

    failed_seasons = []
    results = []

    logger.info(f"Starting collection for {len(seasons)} seasons of {comp_name}...")

    for season in seasons:
        season_id = season.get("season_id")
        if season.get("comp_id") != comp_id and season_id is None:
            logger.error(f"Season {season_id} from {comp_name} ({comp_id}) does not exist!")
            failed_seasons.append({
                "comp_id": comp_id,
                "comp_name": comp_name,
                "season_id": season_id,
                "error": "Season does not exist!"
            })
        else:
            try:
                details = get_season_details(comp_id,season_id,comp_name)
                results.append(details)
                logger.info(f"Successfully processed season with ID {season_id} from {comp_name} (ID:{comp_id})")
            except Exception as e:
                logger.error(f"Failed to process season with ID {season_id} from {comp_name}: {e}")
                failed_seasons.append({
                    "comp_id": comp_id,
                    "comp_name": comp_name,
                    "season_id": season_id,
                    "error": str(e)
                })

    logger.info(f"Season collection completed: "
                f"Successfull: {len(results)} | "
                f"Failed: {len(failed_seasons)}"
                )

    return results, failed_seasons