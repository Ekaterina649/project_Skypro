from typing import Iterator


def filter_by_currency(list_dict_transactions: list, trans_currency: str) -> Iterator[dict]:
    for dict_trans in list_dict_transactions:
        currency_code = dict_trans["operationAmount"]["currency"]["code"]
        if currency_code == trans_currency:
            yield dict_trans


def transaction_descriptions(list_dict_transactions: list) -> Iterator[str]:
    for dict_trans in list_dict_transactions:
        description = dict_trans.get("description")
        yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted_card
