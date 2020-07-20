class Fibonacci():
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        ret_val = self.prev + self.curr
        self.prev = self.curr
        self.curr = ret_val
        if (ret_val > 1000):
            raise StopIteration
        else:
            return ret_val


f = Fibonacci()
try:
    while True:
        print(next(f), end=', ')
except StopIteration:
    print("Thats Fibonacci series for you!!!!")

fibo = Fibonacci()
for num in fibo:
    print(num, end=', ')
print("Thats Fibonacci series for you!!!!")
