# generate two random numbers between 1 and 9

import random

C = 0
while C != 4:
    A = random.randint(1, 9)
    B = random.randint(1, 9)
    C = A*B
    print('A =', A, 'C =', C)
print('Success!')
print('A =', A, 'B =', B)