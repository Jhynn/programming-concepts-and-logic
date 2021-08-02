print('Arithmetic progression.')
a_1 = float(input('What is the first term: '))
reason = float(input('What is the reason: '))
n = int(input('How is the term that you want to know: '))

n_th = a_1 + (n - 1)*reason

print(f'The {n}th term is {n_th}.')
