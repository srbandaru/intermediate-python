import random


def my_randam_generator(iterable):
    my_iter = list(iterable)
    random.shuffle(my_iter)

    while len(my_iter) > 0:
        yield my_iter.pop()


generator = my_randam_generator([1, 2, 3, 4, 5])

for num in generator:
    print(num, end=' ')
