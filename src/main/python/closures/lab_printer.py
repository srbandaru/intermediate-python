def count_wrapper(f):
    def counter(*args, **kwargs):
        count = {}
        for arg in args:
            for letter in arg:
                count[letter] = count.get(letter, 0) + 1
        print(count)
        print("about to execute {}".format(f.__name__))
        f(*args, **kwargs)

    return counter

@count_wrapper
def printer(s):
    print(s)

printer('python programming rocks')