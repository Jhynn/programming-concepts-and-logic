supermarket_1 = list()
supermarket_2 = list()
cheap = list()
product_super_1 = product_super_2 = 0

for _ in range(4):
    print(f'Product ({(_+1)} of 4.)')
    product_super_1 = int(input(f'Type the price, supermarket 1: '))
    product_super_2 = int(input(f'Type the price, supermarket 2: '))

    supermarket_1.append(product_super_1)
    supermarket_1.append(product_super_2)

    if product_super_1 < product_super_2:
        cheap.append('1')

    else:
        cheap.append('2')

print(f'\nThe cheapest way is:\n')

for _ in range(4):
    print(f'Buy the produt {_+1} on supermarket {cheap[_]}.')
