'''
jaffer razavi
oct 26 2019
Unique random numbers
'''
import random

a = random.randint(1,5)
b = random.randint(1,5)
c = random.randint(1,5)
num = 1
hmm = 1


while (a == b) or (a==c) or (b==c):
    print ('Iteration:',a,b,c)
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)

print('Final outcome:',a,b,c)


