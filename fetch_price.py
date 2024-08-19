from requests import Session, ConnectionError, Timeout, TooManyRedirects

def fetch_price_with_ticker(ticker: str) -> list[str, float]:
    # return ['lol', 10000.00]
    """
    Fetches the USD price of a cryptocurrency based on its ticker symbol.

    :param ticker: The ticker symbol of the cryptocurrency (e.g., 'BTC', 'ETH').
    :return: A list containing symbol and USD price if found, None otherwise.
    """
    ticker = ticker.upper()
    usd_price = None
    url = "https://data.messari.io/api/v1/assets?fields=symbol,metrics/market_data/price_usd"
    
    with Session() as session:
        try:
            response = session.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()

            coins = data.get('data', [])
            coin = next((c for c in coins if c['symbol'].upper() == ticker.upper()), None)
            if coin:
                usd_price = coin['metrics']['market_data']['price_usd']

        except KeyError as e:
            print('Key not found', e)
        except IndexError as e:
            print('Index not found', e)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print('Error on request', e)
        except Exception as e:
            print(f'Unexpected error: {e}')

    if usd_price:
        return [ticker, usd_price]
    else:
        return None


if __name__ == "__main__":
    ticker = input("Please enter coin ticker: ")
    if ticker == '' or ticker == None:
        ticker = 'btc'
    result = fetch_price_with_ticker(ticker)
    if result:
        print(f"{result[0]} price is {result[1]:,.2f} USD.")
    else:
        print(f"Symbol '{ticker}' not found.")
