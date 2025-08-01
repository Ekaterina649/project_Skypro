import json
from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


def test_successful_read():
    """Тест успешного чтения файла с корректным JSON-списком"""
    test_data = [{"amount": 100, "currency": "RUB"}, {"amount": 50, "currency": "USD"}]
    json_data = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=json_data)):
        result = get_financial_transactions("test.json")
        assert result == test_data


def test_file_not_found():
    """Тест обработки отсутствия файла"""
    with patch("builtins.open", side_effect=FileNotFoundError()):
        result = get_financial_transactions("nonexistent.json")
        assert result == []


def test_empty_file():
    """Тест обработки пустого файла"""
    with patch("builtins.open", mock_open(read_data="")):
        result = get_financial_transactions("empty.json")
        assert result == []
