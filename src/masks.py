import logging

from src.config import LOGS_DIR

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    LOGS_DIR / 'masks.log', encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция для маскировки номера банковской карты"""
    card_str = str(card_number).replace(" ", "")
    if len(card_str) != 16:
        logger.error(f"Невалидный номер карты: {card_number}")
        raise ValueError
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info(f"Успешная маскировка карты: {masked}")
    return masked


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number).replace(" ", "")
    if not account_number_str.isdigit():
        logger.error(f"Невалидный номер банковского счета: {account_number_str}")
        raise ValueError
    if len(account_number_str) < 4:
        logger.error("Номер счета слишком короткий")
        raise ValueError
    mask = f"**{account_number_str[-4:]}"
    logger.info(f"Успешная маскировка счета {mask}")
    return mask
