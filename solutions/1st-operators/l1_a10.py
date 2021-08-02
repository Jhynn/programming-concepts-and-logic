cost_price = float(input('Type, the cost price of the product: '))

final_price = cost_price + 0.45 * cost_price + 0.5 * cost_price
# Or: final_price = cost_price * 0.95 + cost_price

print(f'The final price will be: $${final_price}.')
