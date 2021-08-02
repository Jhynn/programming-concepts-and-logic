years = int(input('Please, type the amount of years which you smoke: '))
rets = int(input('How many, per day, cigarettes you smoke: '))
pack_price = float(input("How many is a pack of cigarettes (20 'rets): "))

ret_price = pack_price / 20
amount_of_money = rets*ret_price*years*365

print(f'The amount of money that you spent was $${amount_of_money}!')
