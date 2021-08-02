purchased_apples = int(input('How many apples do you want: '))

dollars = 0

if purchased_apples < 12:
    dollars = purchased_apples * 0.4
else:
    dollars = purchased_apples * 0.25

print(f'You need to pay ${dollars}.')
