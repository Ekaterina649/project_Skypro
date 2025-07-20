from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def test_filter_by_currency_correct_value() -> dict:
    """Возвращает словарь с заданным ключом"""
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def test_filter_by_currency_value() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(test_filter_by_currency_correct_value: dict, test_filter_by_currency_value: list) -> None:
    """Получаем первую USD-транзакцию из генератора"""
    result = next(filter_by_currency(test_filter_by_currency_value, "USD"))
    assert result == test_filter_by_currency_correct_value


def test_filter_by_currency_none(test_filter_by_currency_value: list) -> None:
    """Тестирование случая, когда транзакции в заданной валюте отсутствуют."""
    generator = filter_by_currency(test_filter_by_currency_value, "BHY")
    assert list(generator) == []


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        # Пустой список транзакций
        ([], "USD", []),
        # Список без подходящих валют
        (
            [{"operationAmount": {"currency": {"code": "RUB"}}}, {"operationAmount": {"currency": {"code": "EUR"}}}],
            "USD",
            [],
        ),
        # Список с одной подходящей транзакцией
        (
            [{"operationAmount": {"currency": {"code": "RUB"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Список с несколькими подходящими транзакциями
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency_error(
    transactions: List[Dict[str, Any]], currency: str, expected: List[Dict[str, Any]]
) -> None:
    """Параметризованный тест для проверки граничных случаев"""
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.fixture
def test_transaction_descriptions_correct_value() -> str:
    return "Перевод организации"


def test_transaction_descriptions(
    test_filter_by_currency_value: list, test_transaction_descriptions_correct_value: str
) -> None:
    """Проверка, что функция возвращает корректные описания для транзакции"""
    description = next(transaction_descriptions(test_filter_by_currency_value))
    assert description == test_transaction_descriptions_correct_value


@pytest.mark.parametrize(
    "transactions, expected",
    [
        # Пустой список
        ([], []),
        # Одна транзакция с description
        ([{"description": "Оплата услуг"}], ["Оплата услуг"]),
        # Одна транзакция без description
        ([{"id": 1}], [None]),
        # Несколько транзакций с разными сценариями
        (
            [{"description": "Перевод"}, {"id": 2}, {"description": "Пополнение"}],  # Без description
            ["Перевод", None, "Пополнение"],
        ),
        # Все транзакции без description
        ([{"id": 1}, {"id": 2}], [None, None]),
    ],
)
def test_transaction_descriptions(transactions: list, expected: list) -> None:
    """Параметризованный тест для различных сценариев"""
    result = list(transaction_descriptions(transactions))
    assert result == expected


def test_card_number_generator() -> None:
    generator = card_number_generator(5, 8)

    number_1 = next(generator)
    assert number_1 == "0000 0000 0000 0005"

    number_2 = next(generator)
    assert number_2 == "0000 0000 0000 0006"

    number_3 = next(generator)
    assert number_3 == "0000 0000 0000 0007"

    number_4 = next(generator)
    assert number_4 == "0000 0000 0000 0008"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        # Базовые случаи
        (1, 1, ["0000 0000 0000 0001"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
        # Граничные случаи
        (0, 0, ["0000 0000 0000 0000"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        # Диапазоны
        (1234, 1236, ["0000 0000 0000 1234", "0000 0000 0000 1235", "0000 0000 0000 1236"]),
        # Проверка пробелов
        (12345678, 12345678, ["0000 0000 1234 5678"]),
        (123456789012, 123456789012, ["0000 1234 5678 9012"]),
    ],
)
def test_card_number_generator_formatting(start: int, stop: int, expected: list) -> None:
    """Проверяем корректность форматирования номеров карт"""
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_segments() -> None:
    """Проверяем, что каждая часть содержит 4 цифры"""
    for card_number in card_number_generator(10, 20):
        segments = card_number.split()
        assert len(segments) == 4
        for segment in segments:
            assert len(segment) == 4
            assert segment.isdigit()
