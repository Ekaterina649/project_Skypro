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


def actions_user() -> None:
    while True:
        try:
            user_number_card = int(input("Введите номер карты: "))
            mask_card_number = get_mask_card_number(user_number_card)
            print(f"Номер карты: {mask_card_number}")
            break  # Выход из цикла, если карта введена верно
        except ValueError:
            print("Номер карты должен состоять из 16 символов")

    while True:
        try:
            user_account_number = int(input("Введите номер счёта: "))
            mask_account_number = get_mask_account(user_account_number)
            print(f"Номер счёта: {mask_account_number}")
            break
        except ValueError:
            print("Номер счета должен состоять только из цифр, не менее 4!")
