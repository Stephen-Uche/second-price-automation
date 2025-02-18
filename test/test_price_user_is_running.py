from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.resolve() / '.env'

if not env_path.exists():
    raise FileNotFoundError(f"Environment file not found at {env_path}")

load_dotenv(env_path)


def test_service_is_running_health_check_returns_200_status_code(client):
    """Test case to check if the price_quote api module is running."""
    response = client.get('/pricing_quote/v1/')
    assert response.status_code == 200

def test_service_is_running_health_check_returns_valid_api_response(client):
    """Test case to check if the price_quote api module is running."""
    response = client.get('/pricing_quote/v1/')
    assert response.json == {"message": "price_quote API Module"}
