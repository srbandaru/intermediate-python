def make_adder(x):
    print('received {}'.format(x))

    def adder(y):
        """adds two numbers"""
        return x + y

    return adder


adder = make_adder(7)
print(type(adder))
print(adder(6))
print(adder.__doc__)
print(adder.__closure__[0].cell_contents)
