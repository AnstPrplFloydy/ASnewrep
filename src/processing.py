from typing import Dict, List, Union


def filter_by_state(
    list_of_dicts: List[Dict[str, Union[int, str]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str]]]:
    """Функиия, возвращающая список словарей по значению ключа, переданного в аргумент"""
    return [x for x in list_of_dicts if x.get("state") == state]


def sort_by_date(
    list_of_dicts: List[Dict[str, Union[int, str]]], reverse: bool = True
) -> List[Dict[str, Union[int, str]]]:
    """Функция, принимающая список словарей и параметр для его сортировки по значению ключа"""
    return sorted(list_of_dicts, key=lambda list_of_dicts: list_of_dicts["date"], reverse=reverse)
