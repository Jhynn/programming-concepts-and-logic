number = int(input('Enter a number, please: '))

binary = list()

while number != 0:
    binary.append(str(number % 2))
    number //= 2

s = str().join(binary)

print(s[::-1])
