import pytest
from app import create_flask_app
from config import TestingConfig


app = create_flask_app(TestingConfig)

@pytest.fixture
def client():
    """Fixture to provide a test client for the price_quote api module."""
    with app.test_client() as client:
        yield client