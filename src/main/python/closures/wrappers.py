def logging(f):
    print("About to execute {}".format(f.__name__))

    def wrapper(*args, **kwargs):
        print("Calling {}({}, {})".format(f, args, kwargs))
        return f(*args, **kwargs)

    return wrapper


def print_some(*args):  # packing
    for arg in args:  # unpacking
        print(arg, end=' ')


with_logging = logging(print_some)
with_logging("I", "Love", "Python")
