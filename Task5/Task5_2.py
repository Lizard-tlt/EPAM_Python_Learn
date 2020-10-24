# Задание 6.1 - Currency
# Реализовать абстрактный класс валюты Currency, с наследниками Euro, Dollar, Rubble.
from abc import ABC, abstractmethod
from decimal import Decimal as Dec

# Справочник валют
curr_dict = dict(RUR=(u'\u20BD', "Ruble"),
                 EUR=(u'\u20AC', "Euro"),
                 USD=(u'\u0024', "Dollar"))

# Справочник курсов
courses = {("USD", "RUR"): Dec("75.386"),
           ("EUR", "RUR"): Dec("89.292"),
           ("EUR", "USD"): Dec("1.1845"),
           ("USD", "EUR"): Dec("0.8442"),
           ("RUR", "USD"): Dec("0.01325"),
           ("RUR", "EUR"): Dec("0.01119")}


class Currency(ABC):
    """Абстрактный класс вылюты"""

    def __init__(self, iso_code, sum_value):
        super().__init__()

        str_code = curr_dict.get(iso_code)[0]
        if not str_code:
            raise ValueError('Ошибка значения. Валюта не определена!')

        self._iso_code = iso_code
        self._curr_str_code = str_code
        self._curr_name = curr_dict.get(self._iso_code)[1]
        self._sum = Dec(sum_value)

    @staticmethod
    def _course(currency_from, currency_to):
        """
        Получение курса
        :param currency_from: Из какой валюты
        :param currency_to: В какую валюту
        :return: курс
        """
        if not issubclass(currency_from, Currency):
            raise TypeError('Не допустимый класс currency_from!')
        if not TypeError(currency_to, Currency):
            raise TypeError('Не допустимый класс currency_to!')

        if currency_from.iso_code() == currency_to.iso_code():
            return 1
        else:
            key = (currency_from.iso_code(), currency_to.iso_code())
            course = courses.get(key)
            if not course:
                raise ValueError('Не найден курс!')
            return course

    @classmethod
    @abstractmethod
    def iso_code(cls):
        """Заполнение кода валюты в классах-потомках"""
        pass

    @property
    def currency(self):
        """Получение названия валюты"""
        return self._curr_name

    @classmethod
    def course(cls, currency):
        """
        Получение курса
        :param currency: В какую валюту
        :return: Курс
        """
        return cls._course(cls, currency)

    def to(self, currency):
        """
        Конвертация в валюту currency
        :param currency: В какую валюту
        """
        return Currency._course(type(self), currency) * self._sum

    def set_course(self, currency, course_new_value):
        """
        Установка нового курса
        :param currency: В какую валюту
        :param course_new_value: Новое значение курса
        """
        key = (self.iso_code(), currency.iso_code())
        if courses.get(key):
            courses.update({key: Dec(str(round(course_new_value, 5)))})
        else:
            raise ValueError(f'Не найден курс! {key}')

    def get_sum(self, other):
        """
        Получение суммы для операций сравнения
        :param other: Класс Currency или значение
        :return:сумма валюты
        """
        if isinstance(other, Currency) and self.iso_code() != other.iso_code():
            return other.to(type(self))
        else:
            return other

    def __call__(self, value):
        return value

    def __str__(self):
        return f"{self._sum} {self._curr_str_code}"

    def __repr__(self):
        return f"{self._sum} {self._curr_str_code}"

    def __radd__(self, other):
        return self._sum + other

    def __add__(self, other):
        return self._sum + self.get_sum(other)

    def __lt__(self, other):
        return self._sum < self.get_sum(other)

    def __gt__(self, other):
        return self._sum > self.get_sum(other)

    def __le__(self, other):
        return self._sum <= self.get_sum(other)

    def __ge__(self, other):
        return self._sum >= self.get_sum(other)

    def __eq__(self, other):
        return self._sum == self.get_sum(other)

    def __ne__(self, other):
        return self._sum != self.get_sum(other)


class Euro(Currency):
    ISO_CODE = "EUR"

    @classmethod
    def iso_code(cls):
        return cls.ISO_CODE

    def __init__(self, sum_value=0):
        super().__init__(self.ISO_CODE, sum_value)


class Dollar(Currency):
    ISO_CODE = "USD"

    @classmethod
    def iso_code(cls):
        return cls.ISO_CODE

    def __init__(self, sum_value=0):
        super().__init__(self.ISO_CODE, sum_value)


class Ruble(Currency):
    ISO_CODE = "RUR"

    @classmethod
    def iso_code(cls):
        return cls.ISO_CODE

    def __init__(self, sum_value=0):
        super().__init__(self.ISO_CODE, sum_value)


e = Euro(5)
print(e)

print(f"e.to(Dollar) = {e.to(Dollar)}")

print(f"sum([Euro(i) for i in range(5)]) = {sum([Euro(i) for i in range(5)])}", )

print(f"e > Euro(6) {e > Euro(6)}")

print(f"e + Dollar(10) = {e + Dollar(10)}")

print(f"Dollar(10) + e = {Dollar(10) + e}")

print("--- Не так как в задании ---")
usd = Dollar(1)
print(f"usd.to(Ruble) = {usd.to(Ruble)}")
print(f"Ruble.course(Dollar) = {Dollar.course(Ruble)}")
usd.set_course(currency=Ruble, course_new_value=100)
print(f"Ruble.course(Dollar) = {Dollar.course(Ruble)}")
print(f"usd.to(Ruble) = {usd.to(Ruble)}")

print("e.currency ", e.currency)
