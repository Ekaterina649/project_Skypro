import os

import requests
from dotenv import load_dotenv


def transaction_amount_in_rubles(transaction: dict) -> float:
    """Конвертирует сумму в рубли по текущему курсу"""
    load_dotenv()

    API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
    API_BASE_URL = os.getenv("BASE_URL")

    amount = float(transaction["amount"])
    currency = transaction["currency"].upper()

    if currency == "RUB":
        return amount
    else:
        try:
            params = {
                "from": currency,
                "to": "RUB",
                "amount": amount
            }
            headers = {"apikey": API_KEY}
            response = requests.get(API_BASE_URL, headers=headers, params=params)
            status_code = response.status_code
            if status_code == 200:
                result = response.json()["rates"]["RUB"]
                return round(amount * result, 2)
        except Exception as e:
            raise ValueError(f"Currency conversion failed: {str(e)}")



