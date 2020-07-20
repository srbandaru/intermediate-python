from itertools import zip_longest
from itertools import count

strings = ['apple', 'cherry', 'peach']

nums = [1, 2, 3, 4, 5]

for p in zip_longest(nums, strings, fillvalue="******"):
    print(p)

c = count(start=780)

for _ in range(10):
    print(next(c))

counter= count(1, 0.25)

for _ in range(10):
    print(next(counter))
