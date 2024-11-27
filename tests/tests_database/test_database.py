import os
import psycopg2
import pytest
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


@pytest.fixture(scope="session")
def db_connection():
    """Fixture to set up and tear down the database connection"""
    # Establish the database connection
    with psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD) as conn:
        yield conn


def test_connection_established(db_connection):
    assert db_connection is not None, "Connection is not established."
    assert db_connection.closed == 0, "Connection has been closed."


def test_top_10_most_expensive_products(db_connection):
    """Test retrieving the top 10 most expensive products."""
    cursor = db_connection.cursor()
    query = """
    SELECT product_name, unit_price
    FROM products
    ORDER BY unit_price DESC
    LIMIT 10;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Expected results (top 10 products by unit_price)
    expected_results = [
        ('Côte de Blaye', 263.5),
        ('Thüringer Rostbratwurst', 123.79),
        ('Mishi Kobe Niku', 97),
        ('Sir Rodney\'s Marmalade', 81),
        ('Carnarvon Tigers', 62.5),
        ('Raclette Courdavault', 55),
        ('Manjimup Dried Apples', 53),
        ('Tarte au sucre', 49.3),
        ('Ipoh Coffee', 46),
        ('Rössle Sauerkraut', 45.6)
    ]

    # Assert that the results match the expected top 10
    assert results == expected_results
    cursor.close()