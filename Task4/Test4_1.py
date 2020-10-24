# Необходимо написать фабрику декораторов(такжедекоратор).
# Фабрика(функция) принимает аргумент-функцию(lambda) и декоратор.
# Возвращает декоратор, который должен вызывать функцию(lambda) с аргументом-результатом декорируемого декоратора.
import functools as ft


def fabric(lambda_) -> type:
    def fabric_decorator(repeat_deco) -> type:
        def repeat_wrapper(*d_args, **d_kwargs):

            @ft.wraps(repeat_deco)
            def foo_deco(func_):

                @ft.wraps(func_)
                def foo_wrapper(*args, **kwargs):

                    if fabric.decorator_enabled:
                        #  print(lambda_.__name__)
                        return lambda_(repeat_deco(*d_args, **d_kwargs)(func_)(*args, **kwargs))
                    else:
                        return lambda_(func_(*args, **kwargs))

                return foo_wrapper
            return foo_deco
        return repeat_wrapper

    fabric.decorator_enabled = True

    def decorator_switch_off():
        fabric.decorator_enabled = False

    def decorator_switch_on():
        fabric.decorator_enabled = True

    fabric.off = decorator_switch_off
    fabric.on = decorator_switch_on

    return fabric_decorator


@fabric(lambda x: x ** 2)
def repeat(times) -> type:
    # print("value_ ", value_)
    def decorator(func_):

        """ Этот декоратор отключеется """
        def func_wrapper(*args, **kwargs):
            for i in range(times):
                func_(*args, **kwargs)
            return times

        return func_wrapper

    return decorator


@repeat(3)
def foo(x):
    print("Foo called!")
    # Если fabric.off() возвращаемое значение будет нижестоящего return будет аргументом лямбды
    # Если fabric.on() аргумент лямбды будет из параметра декоратора
    return 3


fabric.on()
print(f'Result from decorator = {foo(123)}')


