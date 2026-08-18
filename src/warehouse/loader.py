from sqlalchemy import text
from src.warehouse.connection import engine
import logging

logger = logging.getLogger(__name__)

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
    """)

    with engine.begin() as conn:
        conn.execute(query, competition)

    logger.info(
        f"Loaded competition: {competition["comp_name"]} (ID: {competition["comp_id"]})"
    )    