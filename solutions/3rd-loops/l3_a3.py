# We know that a prime number is divisible just by itself and by 1.

number = int(input('Enter the number: '))

# The penultimate number, because the last is itself and
# every number is divisible by 1 ─ justifying the range.
# 4 / 2 == 2.

if number == 4:
    print('4 is not prime.')
else:
    for x in range(2, int(number/2)):
        if number % x == 0:
            print("Here!")
            print(f'{number} is not prime.')
            break
    else:
        print(f'{number} is prime.')
