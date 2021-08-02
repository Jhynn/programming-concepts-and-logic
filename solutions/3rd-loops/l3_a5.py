number_1 = input("Enter a number: ")
number_2 = input(
    "Enter another number (to see if the 1st is a permutation of it): "
)

permutation = True

if number_1 == number_2:
    print("The numbers are the same.")
else:
    for _ in number_1:
        if _ not in number_2:
            permutation = False
            break

if permutation:
    print("Those are a permutation of each other.")
else:
    print('Those are not a permutation of each other.')
