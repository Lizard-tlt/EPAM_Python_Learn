# Необходимо написать фабрику декораторов(так же декоратор).
# Фабрика(функция) принимает аргумент-функцию(lambda) и декоратор.
# Возвращает декоратор, который должен вызывать функцию(lambda) с аргументом-результатом декорируемого декоратора.
import functools as ft


class Fabric:
    def __init__(self, lambda_):
        self.lambda_ = lambda_

    def __call__(self, repeat_function):
        def repeat_wrapper(*d_args, **d_kwargs):
            # print(repeat_function.__name__)  # repeat

            @ft.wraps(repeat_function)
            def foo_deco(foo_func):
                @ft.wraps(foo_func)
                def foo_wrapper(*args, **kwargs):
                    # print(foo_func.__name__)  # foo
                    return self.lambda_(repeat_function(*d_args, **d_kwargs)(foo_func)(*args, **kwargs))

                return foo_wrapper
            return foo_deco
        return repeat_wrapper


@Fabric(lambda x: x ** 2)
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, foo_func):
        def repeat_foo_wrapper(*args, **kwargs):
            # print(foo_func.__name__)
            for i in range(self.times):
                foo_func(*args, **kwargs)
            return self.times

        return repeat_foo_wrapper


@Repeat(5)
def foo(x):
    print("Foo called!")
    return 3


print(f'Result from decorator = {foo(123)}')
