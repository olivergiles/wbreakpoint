from wb import wb


@wb
def test():
    a = 1
    a += 1
    return a


if __name__ == "__main__":
    print(type(test))
    test()
