from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(nums: str) -> str:
    if "Счет" in nums:

        return get_mask_account(nums[5:])

    else:

        return get_mask_card_number(nums[-16:])

