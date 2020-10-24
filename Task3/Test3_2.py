# Необходимо создать функции
# select(*field_name: list) -> None,
# field_filter(field_name: str, *collection: list) -> None,
# query(*collection, select, field_filter, ...) -> list.
# В 2х вариантах, с циклами и функциональным подходом
from tabulate import tabulate


friends = [
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол'},
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'},
    {'name': 'Василий', 'gender': 'Мужской', 'sport': 'Рыбалка'},
    {'name': 'Лариса', 'gender': 'Женский', 'sport': 'Йога'}
]


def select(*field_names) -> None:
    """
    Филитр по имени поля
    :param field_names: список полей результата
    :return: Функция
    """
    def selector_(field_name: str) -> bool:
        return field_name in field_names
    return selector_


def field_filter(field_name, field_name_values) -> None:
    """
    Фильтрация значений
    :param field_name: Имя поля
    :param field_name_values: Значения поля
    :return: Bool
    """
    def val_in_filter(data) -> bool:
        return data[field_name] in field_name_values
    return val_in_filter


def query_func(data, selector, *filters) -> list:
    """
    Получение результата с использованием функционального подхода
    :param data: Исходный список зачений
    :param selector: Список полей результата
    :param filters: Список значений, которые попадут в результат
    :return: список резулитирующих элементов
    """
    result_query = []
    for row in data:
        # Хм, а без all и map будет больше кода...
        if all(map(lambda filter_func: filter_func(row), filters)):
            result_query.append({k: v for k, v in row.items() if selector(k)})
    return result_query


def query(data, selector, *filters) -> list:
    """
    Получение результата без функционального подхода
    :param data: Исходный список зачений
    :param selector: Список полей результата
    :param filters: Список значений, которые попадут в результат
    :return: список резулитирующих элементов
    """
    result_query = []
    for row in data:
        for filter_func in filters:
            if not filter_func(row):
                break
        else:
            result_query.append({k: v for k, v in row.items() if selector(k)})
    return result_query


if __name__ == "__main__":
    result = query_func(friends,
                        select('name', 'gender', 'sport'),
                        field_filter('gender', ['Мужской', 'Женский']),
                        field_filter('sport', ['Йога', 'Рыбалка']))
    print(tabulate(result, headers='keys', showindex="always", tablefmt="grid"))

