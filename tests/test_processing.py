import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "bank_operations, state, expected",
    [
        # Тест 1: Фильтрация операций со статусом EXECUTED
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        # Тест 2: Фильтрация операций со статусом CANCELED
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        # Тест 3: Проверка случая, когда нет операций с указанным статусом
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "CANCELED",
            [],
        ),
        # Тест 4: Проверка с пустым списком операций
        ([], "EXECUTED", []),
        # Тест 5: Проверка с несуществующим статусом
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "PENDING",
            [],
        ),
    ],
)
def test_filter_by_state(bank_operations: list[dict], state: str, expected: list[dict]) -> None:
    """Тестирование функции filter_by_state."""
    result = filter_by_state(bank_operations, state)
    assert result == expected


@pytest.mark.parametrize(
    "bank_operations, reverse, expected",
    [
        # Тест 1: Сортировка по убыванию дат
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        # Тест 2: Сортировка по возрастанию дат
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        # Тест 3: Сортировка при одинаковых датах
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
        # Тест 4: Пустой список
        ([], True, []),
        # Тест 5: Сортировка с нестандартным форматом дат (YYYY-MM-DD)
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 3, "state": "CANCELED", "date": "2018-09-12"},
            ],
            True,
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 3, "state": "CANCELED", "date": "2018-09-12"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30"},
            ],
        ),
    ],
)
def test_sort_by_date(bank_operations: list[dict], reverse: bool, expected: list[dict]) -> None:
    """Тестирование функции sort_by_date."""
    result = sort_by_date(bank_operations, reverse)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
