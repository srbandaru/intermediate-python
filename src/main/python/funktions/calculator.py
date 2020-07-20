def calculate(func, a, b):
    return func(a, b)


print(calculate(lambda x, y: x + y, 1, 3))
print(calculate(lambda x, y: x * y, 2, 5))
print(calculate(lambda x, y: x / y, 5, 2))
print(calculate(lambda x, y: x // y, 5, 2)) # integer division
print(calculate(lambda x, y: x % y, 5, 2))
