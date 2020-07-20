def fact(n):
    '''returns n!
    '''
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


l = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, l))
factorials = list(map(fact, l))
print(factorials)
print(fact(5))
print(fact.__doc__)
print(type(fact))
print(help(fact))
print(squares)
print(list(map(fact, range(1, 6))))
print([fact(num) for num in range(1, 6, 2)])
