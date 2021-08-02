average_balance = float(input('Type the average balance: $'))
credit_value = None

if average_balance < 200.9:
    credit_value = 0
elif average_balance < 400.9:
    credit_value = 0.2 * average_balance
elif average_balance < 600:
    credit_value = 0.3 * average_balance
else:
    credit_value = 0.4 * average_balance

print(
    f'Your average balance is ${average_balance} and '
    f'credit value is ${credit_value}'
)
