#jaffer Razavi
#oct 11 2019

Age = int(input("How may years old are you? \n"))

if (Age >=17):
    print("You can watch R rated movies")
elif (Age >=13) and (Age <=16):
    print("You can watch PG-13, PG, or G movies")
elif (Age <13) and (Age >=7):
    print("You can watch G or PG rated movies")
elif (Age <7) and (Age >=0):
    print("You can only watch G rated movies")
else:
    print("You are not old enought to buy tickets")

    
