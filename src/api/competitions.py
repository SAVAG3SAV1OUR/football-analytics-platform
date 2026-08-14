from src.api.client import get_data

LEAGUES = "leagues"

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