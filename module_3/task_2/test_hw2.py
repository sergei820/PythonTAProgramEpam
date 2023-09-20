from hw2 import cache


def test_cache():
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2

    val_3 = cache_func(200, 300)
    assert val_1 == (some[0] ** some[1]) ** 2
    assert val_2 == (some[0] ** some[1]) ** 2
    assert val_2 is not val_3
