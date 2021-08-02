joseph = 150    # In cm.
peter = 110
year = 0

while peter <= joseph:
    # If you want to see the development...
    # print(f'{year}th, Peter: {peter}cm and Joseph: {joseph}cm.')
    peter += 3
    joseph += 2
    year += 1

print(
    f'On the {year}th year, Peter ({peter}cm) will be '
    f'more tall than Joseph ({joseph}cm).'
)
