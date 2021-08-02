x_1 = float(input('Type the x_1 coordinate: '))
y_1 = float(input('Type the y_1 coordinate: '))

x_2 = float(input('Type the x_2 coordinate: '))
y_2 = float(input('Type the y_2 coordinate: '))

distance = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5

print(
    f'The distance between P1({x_1}, {y_1}) and P2({x_2}, {y_2}) is {distance}.'
)
