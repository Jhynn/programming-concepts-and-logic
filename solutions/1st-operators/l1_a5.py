print('Please, type...')
hours = int(input('The hours: '))
minutes = int(input('The minutes: '))
seconds = int(input('The seconds: '))

# Remember, 1 hour is equals to 60 minutes which is equals to 60 seconds.
all_in_seconds = hours * 60 * 60

# Based on above, 1 minutes = 60 seconds.
all_in_seconds += minutes * 60

# 1 sec is equals to 1 sec.
all_in_seconds += seconds

# all_in_seconds accumulated and transformed all values in seconds.

# Two more convenient ways would be:

# all_in_seconds = hours*3_600 + minutes*60 + seconds
# all_in_seconds = seconds + 60*(60*hours + minutes)

print(f'{hours}:{minutes}:{seconds} equals to {all_in_seconds} seconds.')
