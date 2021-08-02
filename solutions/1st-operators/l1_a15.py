height = float(input('How tall is the kitchen: '))
width = float(input('How large is the kitchen: '))
length = float(input('How deep is the kitchen: '))

tile_boxes = (height * width * length) / 1.5

print(f'Will be needed {tile_boxes} tile boxes.')
