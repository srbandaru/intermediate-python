from datetime import datetime

def timer(f):
    def inner(*args, **kwargs):
        start = datetime.now()
        value = f(*args, **kwargs)
        time_taken = str(datetime.now() - start)
        print("function {} took {} to execute".format(f.__name__, time_taken))
        return value

    return inner


@timer
def long_running_func(*args):
    def fact(num):
        if num < 2:
            return 1
        else:
            return num * fact(num - 1)

    values = []
    for arg in args:
        for n in arg:
            values.append(fact(n))
    return values


print(long_running_func(range(1, 50)))
