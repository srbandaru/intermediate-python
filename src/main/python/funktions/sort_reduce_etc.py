from functools import reduce

fruits = ['kiwi', 'fig', 'peach', 'pineapple', 'orange']
print(sorted(fruits))
print(sorted(fruits, key=lambda word: len(word)))
print(sorted(fruits, key=lambda word: word[::-1]))

print(reduce(lambda x, y: x + y, range(1, 11)))
