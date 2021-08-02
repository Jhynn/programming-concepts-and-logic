student_id = int(input('Please, type your id: '))
score_1 = float(input('Type your 1st score: '))
score_2 = float(input('Type your 2nd score: '))
score_3 = float(input('Type your 3rd score: '))
exe_avg = float(input('Type your exercise average: '))

au = (score_1 + score_2*2 + score_3*3 + exe_avg) / 7
concept = None
approved = True

if au >= 9:
    concept = 'A'
elif au >= 7.5:
    concept = 'B'
elif au >= 6:
    concept = 'C'
elif au >= 4:
    approved = False
    concept = 'D'
else:
    approved = False
    concept = 'E'

print(f'Concept: {concept}.')

if approved:
    print('Congrates you was approved.')
else:
    print('Unfortunately, you fail. Try again.')
