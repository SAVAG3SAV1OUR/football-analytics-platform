def transform_comps(raw_data):
    tournament = raw_data["data"]["uniqueTournament"]

    return {
        "comp_id": tournament["id"],
        "comp_name": tournament["name"],
        "country": tournament.get("category", {}).get("country", {}).get("name"),
        "tier": tournament.get("tier", {}),
        "has_rounds": tournament.get("hasRounds"),
        "has_groups": tournament.get("hasGroups"),
        "has_playoff_series": tournament.get("hasPlayoffSeries"),
        "logo_id": tournament.get("logo", {}).get("id")
    }