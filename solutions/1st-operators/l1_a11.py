print('Please, pass this informations.')
distance = float(input('How many Km are between the cities: '))
tolls = int(input('How many tolls will you pass: '))

travel_cost = 8*tolls + 2.6*distance/15

print(f'Cost of the travel: $${travel_cost}.')
