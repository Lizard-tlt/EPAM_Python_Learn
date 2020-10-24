# Написать программу имитирующую телефонный справочник.
# Должен быть консольный итерфейс в котором доступно 3 действия : добавить номер и имя человека,
# взять номер человека по имени, удалить человека.
from tabulate import tabulate

phone_book = {}  # Справочник


def add_person(person_name, phone_number) -> None:
    """
    Добавление субъекта
    :param person_name: Имя
    :param phone_number: Телефон
    :return:
    """
    phones = phone_number.split(",")
    if not phone_book.get(person_name):
        phone_book[person_name] = {"name": person_name, "phones": phones}
    else:
        print(f"Субъект {person_name} уже был добавлен.")


def get_person(person_name) -> dict:
    """
    Поиск субъекта
    :param person_name:Имя
    :return:
    """
    return phone_book.get(person_name)


def del_person(person_name) -> None:
    """
    Удаление субъекта
    :param person_name:
    :return:
    """
    try:
        phone_book.pop(person_name)
    except KeyError:
        print(f"Субъект {person_name} для удаления не найден!")


def get_person_name() -> str:
    """
    Запрос имени субъекта
    :return:
    """
    return input('Введите имя: ')


def get_phone_number() -> str:
    """
    Запрос номера телефона субъекта
    :return:
    """
    return input('Введите номер: ')


def show_phone_book() -> None:
    """
    Печать содержимого справочника
    :return:
    """
    print(tabulate(phone_book.values(), headers='keys', showindex="always", tablefmt="grid"))


def add_person_intf() -> bool:
    """ Добавление субъекта c запросом необходимых параметров"""
    person_name = get_person_name()
    phone_number = get_phone_number()
    add_person(person_name, phone_number)
    return True


def get_person_intf() -> bool:
    """ Поиск субъекта c запросом необходимых параметров"""
    found_person = get_person(get_person_name())
    print(f"Найден субъект:  {found_person}")
    return True


def del_person_intf() -> bool:
    """ Удаление субъекта c запросом необходимых параметров"""
    person_name = get_person_name()
    del_person(person_name)
    return True


def error_choice() -> bool:
    print('Не верный выбор!')
    return True


def end_work() -> bool:
    return False


def user_menu() -> None:
    """
    Основная часть интерфейса с пользователем
    :return:
    """
    method = dict([("1", (add_person_intf, "1 - Добавить(номера нескольких телефонора разделяются ',').")),
                   ("2", (get_person_intf, "2 - Получить.")),
                   ("3", (del_person_intf, "3 - Удалить")),
                   ("0", (end_work, "0 -Выход."))
                   ]
                  )

    def get_method(menu_item):
        item = method.get(menu_item)
        return item[0] if item else error_choice

    # Строка меню выбора действия
    menu_help_str = " ".join(map(str, [i[1] for i in method.values()]))

    # Вывод текущего состояния словаря
    show_phone_book()

    operation_num = input(f"Выберите действие : {menu_help_str} :")

    func = get_method(operation_num)
    if func():
        user_menu()


user_menu()
