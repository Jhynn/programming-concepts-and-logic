print('Please, report...')
birth_date_day = 24  # int(input('The which day you born: '))
birth_date_month = 9  # int(input('The which month you born: '))
birth_date_year = 2001  # int(input('The which year you born: '))

print()
current_day = 2  # int(input('The current day: '))
current_month = 8  # int(input('The current month: '))
current_year = 2020  # int(input('The current year: '))

# (day, month, day, month, ...), e.g.: 31, 1 (January); 28, 2 (February)...
# Realize that exists 6 months with 31 days, 5 with 30 and 1 with 28, total 364.

days_month = (31, 1, 28, 2, 31, 3, 30, 4, 30, 5, 30, 6,
              31, 7, 31, 8, 30, 9, 31, 10, 30, 11, 31, 12)

days = current_day - birth_date_day
months = current_month - birth_date_month
years = current_year - birth_date_year

# Normalize the day/month/year quantity, when the current is
# less than the birth date month.
if days < 0:
    days *= -1

if months < 0:
    months += 12
    years -= 1

elif months == 0 and current_day < birth_date_day:
    years -= 1

lived_days = years * 365 + days
# birth_date_month*2 - 1 is used to get the month and its correct
# quantity of days, then calculates the days lived...
month = birth_date_month*2 - 1

# Sum the number of days of each month in the interval defined in the condition.
while days_month[month] != days_month[current_month * 2 - 1]:
    # Remember: 31, 1 (January); 28, 2 (February)...
    days_to_sum = month - 1
    lived_days += days_month[days_to_sum]
    month += 2                  # Go to the next month.

    if month > 23:              # If it pass the last one,
        month = 1               # go back to the begin.

print()
print(f'You have {years} year(s), {months} month(s) and {days} day(s).')
