from src.api.client import get_data
from src.utils.logger import setup_logging
import logging

LEAGUES = "leagues"

setup_logging()
logger = logging.getLogger(__name__)

#Getting tournament ids...
def discover_comps():
    leagues_info = get_data(LEAGUES)

    competitions = []

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

def get_comp_details(comp_id):
    endpoint = f"tournament/{comp_id}/info"

    return get_data(endpoint)

def normalize_comp(details):
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

    return normalize_comp(details)

#Collect all the competitions
def collect_comps_details(limit=None):
    comps = discover_comps()

    if limit:
        comps = comps[:limit]

    failed_comps = []    
    results = []

    logger.info(f"Starting collection for {len(comps)} competitions...")

    for competition in comps:
        comp_id = competition["comp_id"]

        try:
            details = get_comp_details(comp_id)
            normalized = normalize_comp(details)

            results.append(normalized)

            logger.info(f"Successfully processed competition: {comp_id}")
        except Exception as e:
            logger.error(f"Failed to process competition {comp_id}: {e}")

            failed_comps.append({
                "comp_id": comp_id,
                "comp_name": comps["comp_name"],
                "error": str(e)
            })

    logger.info(f"Competition collection completed"
                f"Successfull: {len(results)} | "
                f"Failed: {len(failed_comps)}"
                )

    return results, failed_comps