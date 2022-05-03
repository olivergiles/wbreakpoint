def wb(func):
    def wrapped():
        breakpoint()
        func()
    return wrapped
