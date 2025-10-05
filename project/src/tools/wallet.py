# mock wallet balances (fix this)
wallet_balances = {
    "usd": 0.0,
    "bitcoin": 0.0,
    "ethereum": 0.0
}

transaction_history = []


def buy(command: str):
    """
    Parse a buy command and execute a transaction.
    Example: "buy 0.2 ethereum"
    """
    try:
        parts = command.lower().split()
        usd_value = float(parts[1])
        coin = parts[-1]
        amount = usd_value * 1 # mock conversion rate (fix this)

        if usd_value > wallet_balances["usd"]:
            return {"status": "failed", "reason": "Insufficient USD balance"}

        wallet_balances["usd"] -= usd_value
        wallet_balances[coin] = wallet_balances.get(coin, 0.0) + amount
        transaction_history.append({
            "type": "buy",
            "coin": coin,
            "amount": amount,
            "usd_value": usd_value
        })

        return {
            "status": "success",
            "invested_amount": amount,
            "coin": coin,
            "new_balances": wallet_balances.copy()
        }

    except Exception as e:
        return {"status": "failed", "reason": str(e)}


def sell(command: str) -> dict:
    """
    Parse a sell command and execute a transaction.
    Example: "sell 0.2 ethereum"
    """
    try:
        parts = command.lower().split()
        amount = float(parts[1])
        coin = parts[-1]

        if amount > wallet_balances.get(coin, 0):
            return {"status": "failed", "reason": f"Not enough {coin} to sell"}

        usd_value = amount * 1 # mock conversion rate (fix this)

        wallet_balances[coin] -= amount
        wallet_balances["usd"] += usd_value

        transaction_history.append({
            "type": "sell",
            "coin": coin,
            "amount": amount,
            "usd_value": usd_value
        })

        return {
            "status": "success",
            "sold_amount": amount,
            "coin": coin,
            "usd_received": usd_value,
            "new_balances": wallet_balances.copy()
        }

    except Exception as e:
        return {"status": "failed", "reason": str(e)}


def get_balance(coin: str = None) -> dict:
    if coin:
        return {coin: wallet_balances.get(coin, 0.0)}
    return wallet_balances.copy()


def get_portfolio_value() -> float:
    total = wallet_balances.get("usd", 0)
    for coin, amt in wallet_balances.items():
        if coin != "usd":
            total += amt  # replace with actual market price call
    return total


def list_holdings() -> list:
    return [{"coin": coin, "amount": amt} for coin, amt in wallet_balances.items() if amt > 0]
