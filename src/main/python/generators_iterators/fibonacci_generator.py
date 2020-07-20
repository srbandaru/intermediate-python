def fibonacci():
    curr, prev = 1, 0
    while True:
        ret_val = curr + prev
        yield ret_val
        prev = curr
        curr = ret_val


f = fibonacci()
for num in range(1, 100):
    print(next(f), end=' ')
