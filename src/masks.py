def get_mask_card_number(card_number: int) -> str:
    """Функция для маскировки номера банковской карты"""
    card_str = str(card_number).replace(" ", "")
    if len(card_str) != 16:
        raise ValueError
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number).replace(" ", "")
    if not account_number_str.isdigit():
        raise ValueError
    if len(account_number_str) < 4:
        raise ValueError
    return f"**{account_number_str[-4:]}"



