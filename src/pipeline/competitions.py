from src.api.competitions import collect_comps_details
from src.transformations.competitions import transform_comps
from src.utils.file_handler import save_to_parquet
from src.config import SILVER_DATA_DIR
from src.utils.logger import setup_logging
import logging
import pandas as pd

setup_logging()
logger = logging.getLogger(__name__)

def process_comp_details(limit=None):
    raw_comps, failed_comps = collect_comps_details(limit)

    cleaned_comps = []

    for comp in raw_comps:
        try:
            cleaned = transform_comps(comp)
            cleaned_comps.append(cleaned)
        except Exception as e:
            logger.error(f'Failed to transform competition: {e}')

    df = pd.DataFrame(cleaned_comps)
    df["tier"] = df["tier"].astype("Int64")

    output_path = (SILVER_DATA_DIR / "competitions" / "competitions.parquet")

    save_to_parquet(df, output_path)
    logger.info("===========================================================================")
    logger.info(f"Competition Data saved to {output_path}")
    logger.info("===========================================================================")

    return cleaned_comps, failed_comps