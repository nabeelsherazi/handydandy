def timeit(func):
    """ Function decorator to print run time in console window. """
    def wrapper(*args, **kwargs):
        t0 = time.clock()
        func(*args, **kwargs)
        t1 = time.clock()
        print("Completed in {0:.2f} seconds.".format(t1 - t0))
    return wrapper


def loud(func):
    """Function decorator that makes func print the arguments its called with"""
    def wrapper(*args, **kwargs):
        print("arguments:", *args, "keyword arguments:", **kwargs)
        func(*args, **kwargs)
    return wrapper
