from src.masks import get_mask_account, get_mask_card_number

from datetime import datetime


def mask_account_card(nums: str) -> str:
    """Функция, маскирующая номер счета или карты"""
    if "Счет" in nums:
        account_mask = get_mask_account(nums[5:])
        return f"{nums[:4]} {account_mask}"

    else:
        card_mask = get_mask_card_number(nums[-16:])
        return f"{nums[:-17]} {card_mask}"


def get_date(string_with_date: str) -> str:
    """Функция, возвращающая дату"""
    searched_date = datetime.strptime(string_with_date, "%Y-%m-%dT%H:%M:%S.%f")
    return searched_date.strftime("%d.%m.%Y")
