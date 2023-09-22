"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def cache_func(*args):
        if args in cached_results:
            return cached_results[args]
        else:
            result = func(*args)
            cached_results[args] = result
        return result

    return cache_func


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

val_3 = cache_func(200, 300)
# assert val_1 == (some[0] ** some[1]) ** 2
# assert val_2 == (some[0] ** some[1]) ** 2
# assert val_2 is not val_3