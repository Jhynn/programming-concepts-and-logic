money = int(input('How many money: $$'))  # Let $$98

# Remember - // means floor division.
note_100 = money // 100     # 98 // 100 = 0 notes of $$100.00
money %= 100                # The remainder will be $$98.00

note_50 = money // 50       # 98 // 50 = 1
money %= 50                 # money (98) = 98 % 50 = 48

note_20 = money // 20       # 48 // 20 = 1
money %= 20                 # money = 8

note_10 = money // 10       # 8 // 10 = 0
money %= 10                 # money = 8

note_5 = money // 5         # 8 // 5 = 1
money %= 5                  # money = 3

note_2 = money // 2         # 3 // 2 = 1
money %= 2                  # money = 1

note_1 = money // 1         # 1 // 1 = 1
money %= 1                  # money = 0

print(f'{note_100} Note(s) of $$100.00')
print(f'{note_50} Note(s) of $$50.00')
print(f'{note_20} Note(s) of $$20.00')
print(f'{note_10} Note(s) of $$10.00')
print(f'{note_5} Note(s) of $$5.00')
print(f'{note_2} Note(s) of $$2.00')
print(f'{note_1} Note(s) of $$1.00')
