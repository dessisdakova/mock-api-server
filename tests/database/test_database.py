import os
from pathlib import Path
import psycopg2
import pytest
from dotenv import load_dotenv
from common.data_loader import load_test_data


@pytest.fixture(scope="session")
def db_connection():
    """Fixture to set up and tear down the database connection before and after all tests"""
    # Load environment variables from .env file

    env_path = Path(__file__).parent / "db.env"
    load_dotenv(dotenv_path=env_path)

    db_params = {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }

    with psycopg2.connect(**db_params) as conn:
        yield conn


@pytest.fixture(scope="function")
def db_cursor(db_connection):
    """Fixture to create and close a cursor for each test"""
    with db_connection.cursor() as cursor:
        yield cursor


@pytest.mark.parametrize("test_data", load_test_data("test_data_db.json", "queries"))
def test_provided_queries(db_cursor, test_data):
    # act
    db_cursor.execute(test_data["query"])
    actual = db_cursor.fetchall()
    expected = [tuple(row) for row in test_data["expected_results"]]

    # assert
    assert actual == expected
