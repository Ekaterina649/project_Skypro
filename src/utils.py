import json
import logging
from logging import DEBUG
from typing import Any, Dict, List

logger = logging.getLogger("utils")
logger.setLevel(DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/Huawei/PycharmProjects/PythonProject2/logs/utils.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(filename: str) -> List[Dict[str, Any]]:
    """Функция читает файл json и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(filename, encoding="utf-8") as f:
            try:
                logger.info(f"Чтение файла {filename}")
                data = json.load(f)
                if isinstance(data, list):
                    logger.info(f"Успешно прочитано {len(data)} транзакций.")
                    return data
                else:
                    logger.warning("Файл не содержит данные в нужном формате")
                    return []
            except json.JSONDecodeError:
                logger.error("Файл содержит неверный JSON")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []


print(get_financial_transactions("C:/Users/Huawei/PycharmProjects/PythonProject2/data/opertations.json"))
