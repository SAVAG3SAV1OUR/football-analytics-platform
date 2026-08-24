from sqlalchemy import text
from src.warehouse.connection import engine
from src.utils.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

#Load a single competition (Testing)
def load_comps(competition):
    query = text("""
        INSERT INTO warehouse.dim_competition (
            comp_id,
            comp_name,
            country,
            tier,
            has_rounds,
            has_groups,
            has_playoff_series,
            logo_id
        )
        VALUES (
            :comp_id,
            :comp_name,
            :country,
            :tier,
            :has_rounds,
            :has_groups,
            :has_playoff_series,
            :logo_id
        )
        ON CONFLICT(comp_id)
        DO UPDATE SET
            comp_name = :comp_name,
            country = :country,
            tier = :tier,
            has_rounds = :has_rounds,
            has_groups = :has_groups,
            has_playoff_series = :has_playoff_series,
            logo_id = :logo_id
    """)

    with engine.begin() as conn:
        conn.execute(query, competition)

    logger.info(
        f"{competition["comp_name"]} with ID: {competition["comp_id"]} successfully loaded."
    )    


def load_all_competitions(competitions):
    successful = 0
    failed = 0

    failed_list = []

    for competition in competitions:
            try:
                comp_id = competition["comp_id"]
                comp_name = competition["comp_name"]

                load_comps(competition)
                successful +=1
            except Exception as e:
                logger.error(f"{comp_name} with ID({comp_id}) failed to load: {e}")
                failed_list.append({
                    "comp_id": comp_id,
                    "comp_name": comp_name,
                    "error": str(e)
                })
                failed +=1

    logger.info("Competition loading complete")
    logger.info(f"Successful: {successful}")
    logger.info(f"Failed: {failed}")

    return failed_list