#jaffer Razavi
#Oct 11 2019

Num = int(input("Pick a number from 1 to 10 \n"))

if (Num <= 10) and (Num >= 1):
    if(Num >=9) and (Num <=10):
        print("You are in color group Black")
    elif(Num >=7) and (Num <=18):
        print("You are in color group Red")
    elif(Num >=5) and (Num <=6):
        print("You are in color group Light Yellow")
    elif(Num >=3) and (Num <=4):
        print("You are in color group Pink")
    elif(Num >=1) and (Num <=2):
        print("You are in color group Blue")
else:
    print("Invalid Entry")
