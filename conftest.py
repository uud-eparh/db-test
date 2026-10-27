import os
import pytest
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_conn_params():
    return dict(
        host=os.getenv("PG_HOST", "localhost"),
        port=int(os.getenv("PG_PORT", "6432")),
        user=os.getenv("PG_USER", "testuser"),
        password=os.getenv("PG_PASSWORD", "testpass"),
        dbname=os.getenv("PG_DB", "testdb"),
        connect_timeout=5,
    )

@pytest.fixture(scope="session")
def db_conn():
    with psycopg.connect(**get_conn_params()) as conn:
        yield conn