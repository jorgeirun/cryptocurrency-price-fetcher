import pytest, requests

def test_fetch_price_with_ticker():
    response = make_request()
    # Validation of status code  
    assert response.status_code == 200  
    result = response.json()  
    # Assertion of body response content:  
    assert len(result) > 0  
    assert result["data"] is not None


def make_request():
    base_url = "https://data.messari.io/api/v1/assets?fields=symbol,metrics/market_data/price_usd"
    response = requests.get(f'{base_url}')
    return response