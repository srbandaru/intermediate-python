from functools import lru_cache


@lru_cache(maxsize=32)  # defaults to 128
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


print([fact(n) for n in range(1, 11)])

print(fact.cache_info())
