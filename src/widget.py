from masks import get_mask_account, get_mask_card_number

def mask_account_card(str_account):
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    account_details = str_account.split(' ')
    for detail in account_details:
        if detail.lower().startswith("счет"):
            digit_part = next((d for d in account_details if d.isdigit()), None)
            return f"Счет {get_mask_account(digit_part)}"
    for detail in account_details:
        if detail.isdigit():
            card_name = ' '.join([part for part in account_details if not part.isdigit()])
            return f"{card_name}  {get_mask_card_number(detail)}"




print(mask_account_card("Maestro Classic 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
