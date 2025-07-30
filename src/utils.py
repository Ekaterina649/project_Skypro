import json
from typing import List, Dict, Any


def get_financial_transactions(filename: str) ->  List[Dict[str, Any]]:
    """Функция читает файл json и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(filename, encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    print("Файл содержит данные не форме списка")
                    return []
            except json.JSONDecodeError:
                print("Файл содержит неверный JSON")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

