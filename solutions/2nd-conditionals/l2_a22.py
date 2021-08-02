employe_name = input('Type the name of the employe: ')
selled_products = int(input(f'How many products {employe_name} selled: '))

comission = 0

if selled_products < 250:
    comission = selled_products
elif selled_products < 500:
    comission = selled_products * 1.5
else:
    comission = selled_products * 2

print(f"The comission of {employe_name} is ${comission}! Congrats.")
