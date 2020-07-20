s="antidisestablishment"

iterator = iter(s)

try:
    while True:
        str=next(iterator)
        print(str)
except StopIteration:
    print("done!!!")

for letter in s:
    print(letter)
print("done!!")
