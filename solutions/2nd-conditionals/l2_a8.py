number = int(input('Type a (natural) number: '))

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December",)

if number < 0 or number > 12:
    print('Number invalid to be a month.')
else:
    print(f'The correspond month is {months[number-1]}.')
