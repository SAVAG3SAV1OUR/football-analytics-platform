from src.config import DB_URL
from sqlalchemy import create_engine,text


engine = create_engine(DB_URL)

#Testing
def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return result.scalar()
