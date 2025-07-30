from functools import wraps
from typing import Any


def log(filename=None):
    """Декоратор для логирования вызовов функций и их результатов.

    Логирует успешное выполнение функции или возникшие исключения.
    Вывод может быть направлен в файл или в консоль."""
    def decorators_func(func):
        wraps(func)

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message)
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error {type(e).__name__}. Inputs {args},{kwargs}"
                if filename:
                    with open(filename, "a") as f2:
                        f2.write(error_message)
                else:
                    print(error_message)
                raise

        return wrapper

    return decorators_func


@log()
def my_function(x, y):
    return x + y
