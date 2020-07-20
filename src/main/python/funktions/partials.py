from functools import partial

sorted_r = partial(sorted, key=lambda w: w[::-1])

print_no_nl = partial(print, end=' ')
print_no_sp = partial(print_no_nl, sep='-')

print_no_sp("yay..")
print_no_sp("yippie")

print_no_nl("I am")
print_no_nl("Loving Python")


def multiplier(a, b):
    return a * b


doubler = partial(multiplier, b=2)

print(doubler(5))

fruits = ['kiwi', 'fig', 'peach', 'pineapple', 'orange']

print(sorted_r(fruits))
