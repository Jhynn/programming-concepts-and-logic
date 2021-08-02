# Below two ways to solve the problem.
# The 1st one is more intuitive and dumb...
# In contrast the 2nd one is more clever.

number = int(input('Type a number: '))
auxiliar = number
reversed_number = 0

while auxiliar > 0:
    digit = auxiliar % 10
    reversed_number = reversed_number*10 + digit
    auxiliar = auxiliar // 10

if number == reversed_number:
    print("The number is a palindrome!")

else:
    print("The number isn't a palindrome!")


auxiliar = number
limit = number // 2
first = last = counter = 0
palindrome = True
order = 10

if number < 10:
    palindrome = False

else:
    while order < number:
        order *= 10

    order //= 10

    while counter < limit:
        first = auxiliar // order
        last = auxiliar % 10

        if first != last:
            palindrome = False
            break

        counter += 1

if palindrome:
    print(f'{number} is a palindrome.')

else:
    print(f'{number} is not a palindrome.')
