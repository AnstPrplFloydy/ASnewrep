from typing import Dict, List, Union


def filter_by_state(
    list_of_dicts: List[Dict[str, Union[int, str]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str]]]:
    """Функиия, возвращающая список словарей по значению ключа, переданного в аргумент"""
    return [x for x in list_of_dicts if x.get("state") == state]

