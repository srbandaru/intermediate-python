from random import randint


class MyRandomIterator():
    def __init__(self, data):
        self.data = data
        self.counter = len(data)

    def __next__(self):
        if len(self.data) == 0:
            raise StopIteration

        next_val = self.data[randint(0, len(self.data)) - 1]
        self.data.remove(next_val)
        return next_val

    def __iter__(self):
        return self


iterator = MyRandomIterator([1, 2, 3, 4 ,5])

try:
    print('[ ', end='')
    while True:
        print(iterator.__next__(), end=' ') # next(iterator) === iterator.__next__()
except StopIteration:
    print(']')

itr = MyRandomIterator([1, 2, 3, 4, 5])
for num in itr:
    print(num)
