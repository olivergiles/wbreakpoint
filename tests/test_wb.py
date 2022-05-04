from wbreakpoint.wb import wb


@wb
def add_one(x):
    return x + 1


def add_two(x):
    return x + 2


def test_wb():
    assert type(add_one) == type(add_two)
