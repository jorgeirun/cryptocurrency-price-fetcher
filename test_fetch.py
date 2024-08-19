from unittest.mock import patch, Mock
from requests import Session
from fetch_price import fetch_price_with_ticker


@patch.object(Session, 'get')
def test_fetch_price_success(mock_get):
    # Mock the response from the API for a successful fetch
    mock_response = Mock()
    mock_response.json.return_value = {
        'data' : [
            {
                'symbol': 'BTC',
                'metrics': {
                    'market_data': {
                        'price_usd': 100000.0
                    }
                }
            }
        ]
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    result = fetch_price_with_ticker('btc')
    assert result == ['BTC', 100000.0]


@patch.object(Session, 'get')
def test_fetch_price_symbol_not_found(mock_get):
    # Mock the response from the API when the symbol is not found
    mock_response = Mock()
    mock_response.json.return_value = {
        'data': [
            {
                'symbol': 'ETH',
                'metrics': {
                    'market_data': {
                        'price_usd': 5000.0
                    }
                }
            }
        ]
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = fetch_price_with_ticker('XXX')
    assert result is None


@patch.object(Session, 'get')
def test_fetch_price_key_error(mock_get):
    # Simulate a KeyError in the response
    mock_response = Mock()
    mock_response.json.return_value = {
        'data': [
            {
                'symbol': 'BTC'
                # 'metrics' key is missing here
            }
        ]
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = fetch_price_with_ticker('btc')
    assert result is None