""" Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
 """

from typing import Callable


def run_multiple_times(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
                print(result)

            return result

        return wrapper

    return decorator


#@run_multiple_times(3)
def example_function():
    return "Hello, world!"


#example_function()

run_multiple_times(3)(example_function)()