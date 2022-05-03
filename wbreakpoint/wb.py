def wb(func):
    def wrapped():
        """Function to make breakpoint work as a decorator"""
        breakpoint()
        func()

    return wrapped
