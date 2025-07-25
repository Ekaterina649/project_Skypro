from typing import Any

import pytest

from src.decorators import log, my_function


def test_log_correct_value(capsys) -> None:
    """Тест обработки правильных аргументов"""
    my_function(9, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


@pytest.mark.parametrize(
    "x,y,mess_error",
    [
        ("123", 9, True),
        ("a", 8, True),
        ("kk", "78", False),
        ("    ", " ", False),
    ],
)
def test_log_err(x: Any, y: Any, mess_error: bool) -> None:
    """Тест обработки исключений и верных значений"""
    if mess_error:
        with pytest.raises(TypeError):
            my_function(x, y)
    else:
        assert isinstance(my_function(x, y), str)


def test_log_decorator_error(capsys) -> None:
    """Тест обработки исключения с выводом в консоль"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "divide error ZeroDivisionError" in captured.out
    assert "Inputs (1, 0),{}" in captured.out
