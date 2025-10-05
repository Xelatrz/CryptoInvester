import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def get_price(symbol: str) -> float:
    url = f"{BASE_URL}/simple/price"
    params = {"ids": symbol.lower(), "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()

    if symbol.lower() in data:
        return data[symbol.lower()]["usd"]
    else:
        raise ValueError(f"Symbol '{symbol}' not found.")

def get_market_data(symbol: str) -> dict:
    url = f"{BASE_URL}/coins/{symbol.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch market data for '{symbol}'")
    return response.json()

def search_coin(query: str) -> list:
    url = f"{BASE_URL}/search"
    params = {"query": query}
    response = requests.get(url, params=params)
    return response.json().get("coins", [])
