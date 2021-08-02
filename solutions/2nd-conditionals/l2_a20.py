pollution_index = float(input('Type the pollution index: '))

if pollution_index < 0.3:
    print('The index is accetable!')
elif pollution_index < 0.4:
    print('The industries of the 1st group must stop their activies!')
elif pollution_index < 0.5:
    print('The industries of the 1st and 2nd groups must stop their activies!')
else:
    print('All the ─ fuckin\' ─ industries groups must stop their activies!')
