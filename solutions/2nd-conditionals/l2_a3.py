score_1 = float(input('Type your 1st score: '))
score_2 = float(input('Type your 2nd score: '))

average = (score_1 + score_2) / 2

print(f'Your average is {average}, therefore you...')
print('Pass. Congrats.') if average > 6 \
    else print('Fail. Study again, you\'ll get it. :)')
