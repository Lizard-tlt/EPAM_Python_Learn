# Задание 6.1 - Prop descriptor
# Реализовать дескриптор prop aka `property` в виде декоратора.

class prop:
    def __init__(self, function):
        self.func_getter = function

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.func_getter(instance)

    def __set__(self, instance, value):
        if instance is None:
            return self
        return self.func_setter(instance, value)

    def setter(self, function):
        self.func_setter = function


class Something:
    def __init__(self, x):
        self.x = x

    @prop
    def prop(self):
        return self.x ** 2

    @prop.setter
    def attr_setter(self, update):
        self.x = update


c = Something(10)
print(c.prop)
c.prop = 11
print(c.prop)
