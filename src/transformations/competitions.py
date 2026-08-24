from src.utils.logger import setup_logging
import logging


setup_logging()
logger = logging.getLogger(__name__)


def transform_comps(raw_data):
    tournament = raw_data["data"]["uniqueTournament"]

    comp_id = tournament["id"]
    comp_name = tournament["name"]
    country = tournament.get("category", {}).get("country", {}).get("name")
    tier = tournament.get("tier")
    has_rounds = tournament.get("hasRounds")
    has_groups = tournament.get("hasGroups")
    has_playoff_series = tournament.get("hasPlayoffSeries")
    logo_id = tournament.get("logo", {}).get("id")


    if isinstance(comp_name, str):
        comp_name = comp_name.strip()

    if isinstance(country, str):
        country = country.strip()

    if comp_id is not None and not isinstance(comp_id, int):
        logger.error(f"Invalid competition ID: {comp_id}")
        raise ValueError(f"Invalid competition ID: {comp_id}")

    if comp_name is not None and not isinstance(comp_name, str):
        logger.error(f"Invalid competition name: {comp_name}")
        raise ValueError(f"Invalid competition name: {comp_name}")

    if tier is not None and not isinstance(tier, int):
        logger.error(f"Invalid competition tier: {tier}")
        raise ValueError(f"Invalid competition tier: {tier}")

    if logo_id is not None and not isinstance(logo_id, int):
        logger.error(f"Invalid logo ID: {logo_id}")
        raise ValueError(f"Invalid logo ID: {logo_id}")

    #Required fields
    if comp_id is None:
        logger.error("Competition ID is missing")
        raise ValueError(f"Competition ID is mssing")

    if comp_name is None or comp_name == "":
        logger.error("Competition Name is missing")
        raise ValueError("Competition Name is missing")


    return {
        "comp_id": comp_id,
        "comp_name": comp_name,
        "country": country,
        "tier": tier,
        "has_rounds": has_rounds,
        "has_groups": has_groups,
        "has_playoff_series": has_playoff_series,
        "logo_id": logo_id
    }