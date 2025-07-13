import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "str_account, expected",
    (
        ["Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"],
        ["Maestro 1596837868705199", "Maestro 1596 83** **** 5199"],
        ["Счет 73654108430135874305", "Счет **4305"],
        ["Счет 35383033474447895560", "Счет **5560"],
    ),
)
def test_mask_account_card(str_account: str, expected: str) -> None:
    """Тестирование, корректного применения нужного типа маскировки в зависимости от типа входных данных"""
    assert mask_account_card(str_account) == expected


@pytest.mark.parametrize(
    "bad_input",
    [
        "Visa 1234",
        "Счет 456",
    ],
)
def test_mask_account_card_raises(bad_input: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(bad_input)


def test_mask_account_card_no_digits() -> None:
    """Тестирование случая, когда передаваемое значение ни похоже ни на карту ни на счет"""
    assert mask_account_card("Строка") == "Ошибка: неверный формат данных"


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2025-07-12T10:30:00Z", "12.07.2025"),
        ("2020-02-29T23:59:59", "29.02.2020"),
        ("1999-12-31", "31.12.1999"),
        ("0001-01-01T00:00:00", "01.01.0001"),
        ("9999-12-31T23:59:00+05:00", "31.12.9999"),
    ],
)
def test_get_date(data: str, expected: str) -> None:
    assert get_date(data) == expected


@pytest.mark.parametrize(
    "bad_src",
    [
        "",
        "T15:00:00",
        "2025/07/12",
        "2025-07",
        "просто текст",
    ],
)
def test_get_date_bad(bad_src: str) -> None:
    """При невозможности распарсить дату функция должна выбросить ValueError."""
    with pytest.raises(ValueError):
        get_date(bad_src)
