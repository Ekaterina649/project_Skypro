def filter_by_state(bank_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_transactions = []

    for operation in bank_operations:
        if operation.get("state") == state:
            filtered_transactions.append(operation)

    return filtered_transactions


def sort_by_date(bank_operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по дате."""
    return sorted(bank_operations, key=lambda x: x["date"], reverse=reverse)
