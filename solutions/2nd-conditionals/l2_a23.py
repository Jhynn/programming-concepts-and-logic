someone_name = input("Type the name of the mentioned 'somenone': ")
pollution_index = float(input('Type the pollution index: '))
population = int(input('Type the poplation of the city: '))

if pollution_index < 35 and population < 20_000:
    print('This city is "good" for you!')
elif pollution_index < 61 and population < 20_000:
    print('This city is "reasonable" for you!')
elif pollution_index > 34 and population > 40_000:
    print('This city is "bad" for you!')
elif pollution_index > 60 and population > 100_000:
    print('This city sucks for you!')
else:
    print("I cannot define what this city is for you...")
