"""
Jaffer Razavi
oct 24, 2019
Random flowchart stuff
"""

import math

Value = 0
Remain = 0

for i in range (1,101):
    Value = math.sqrt(i)
    Remain = Value % 1
    if (Remain == 0):
        print (i)

print("Thank You")
