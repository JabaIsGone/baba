from datetime import datetime
from typing import List, Dict


def filter_by_state(list_of_value: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей, оставляя только элементы с состоянием 'EXECUTED'.

    :param list_of_value: Список словарей, содержащих ключ 'state'.
    :return: Новый список, содержащий только элементы с 'state' == 'EXECUTED'.
    """
    new_list = []
    for item in list_of_value:
        if item.get("state") == "EXECUTED":
            new_list.append(item)
    return new_list


def sort_by_date(data: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей, содержащих ключ 'date'.
    :param descending: Если True, сортировка по убыванию, иначе по возрастанию.
    :return: Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)
