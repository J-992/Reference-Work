#jaffer Razavi
#oct 20 2019
# input/output loops

Start = int(input("Input a starting value \n"))
Stop = int(input("Input a stopping value \n"))
Count = int(input("Input a step/counting value \n"))
SubAdd = '0' #This subadd makes sure the loop prints the stopping value



if (Count < 0):
    SubAdd = -1
else:
    SubAdd = 1
    

for i in range (Start,Stop+SubAdd,Count):
    print (i)
