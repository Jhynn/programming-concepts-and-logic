number_of_hamsters = int(input('Type the number of hamsters, to stop type '
                                'a non-natural number: '))

while number_of_hamsters:
    cost = (number_of_hamsters * 0.8) / 2 + 10
    print(f'The cost is U${cost}')

    number_of_hamsters = int(input('Type the number of hamsters, to stop type '
                                'a non-natural number: '))
