from src.api.client import get_data
from src.utils.logger import setup_logging
from src.utils.file_handler import save_raw_comps, load_raw_comps, save_league_data, load_league_data
import logging

LEAGUES = "leagues"

# logging
setup_logging()
logger = logging.getLogger(__name__)

# Getting tournament ids...
def discover_comps():
    leagues_info = load_league_data()
    competitions = []

    logger.info("==========================================================================")
    if leagues_info is not None:
        logger.info("Using cached data for league data")
    else:
        logger.info("No cached league data found")
        leagues_info = get_data(LEAGUES)
        save_league_data(leagues_info)


    for country in leagues_info.get("countries",[]):
        for league in country.get("leagues", []):
            competitions.append({
                "comp_id": league["id"],
                "comp_name": league["name"],
                "slug": league["slug"],
                "country": league.get("countryName"),
                "category": league.get("categoryId")
            })


    return competitions

# Info about competitions
def get_comp_details(comp_id):
    endpoint = f"tournament/{comp_id}/info"

    cached_data = load_raw_comps(comp_id)

    if cached_data is not None:
        logger.info(f"Using cached data for competition: {comp_id}")
        return cached_data

    details = get_data(endpoint)
    save_raw_comps(comp_id, details)

    return details


"""def normalize_comp(details):
    comp = details["data"]["uniqueTournament"]

    return {
        "comp_id": comp["id"],
        "comp_name": comp["name"],
        "country": comp.get("category", {}).get("country", {}).get("name"),
        "tier": comp.get("tier"),
        "has_rounds": comp.get("hasRounds"),
        "has_groups": comp.get("hasGroups"),
        "has_playoff_series": comp.get("hasPlayoffSeries"),
        "logo_id": comp.get("logo", {}).get("id")
    }

def get_comps(comp_id):
    details = get_comp_details(comp_id)

    return normalize_comp(details)"""

#Collect all the competitions
def collect_comps_details(limit=None):
    comps = discover_comps()

    if limit:
        comps = comps[:limit]

    failed_comps = []    
    results = []
    logger.info("=======================================================================")
    logger.info(f"Starting collection for {len(comps)} competitions...")

    for competition in comps:
        comp_id = competition.get("comp_id")
        comp_name = competition.get("comp_name")

        if comp_id is None or type(comp_id) is not int or comp_name is None:
            logger.error(f"{comp_name} with ID ({comp_id}) does not exist!")
            failed_comps.append({
                "comp_id": comp_id,
                "comp_name": comp_name,
                "error": "Invalid competition ID or name"
            })
        else:
            try:
                details = get_comp_details(comp_id)

                results.append(details)

                logger.info(f"Successfully processed competition: {comp_id}")
            except Exception as e:
                logger.error(f"Failed to process competition {comp_id}: {e}")

                failed_comps.append({
                    "comp_id": comp_id,
                    "comp_name": comp_name,
                    "error": str(e)
                })

    logger.info(f"Competition collection completed: "
                f"Successfull: {len(results)} | "
                f"Failed: {len(failed_comps)}"
                )

    return results, failed_comps