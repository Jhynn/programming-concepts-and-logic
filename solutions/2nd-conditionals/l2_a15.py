base_salary = float(input('How many is your base salary: $'))

base_salary += base_salary * 0.05                   # Bonus,
base_salary -= 0.07*base_salary                     # Tax,

print(f'Salary to be received: ${base_salary}')     # Actual salary.
