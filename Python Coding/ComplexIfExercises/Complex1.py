#jaffer Razavi
#Oct 4 2019

Grd = float(input("What is your mark in the course? \n"))

#It is a float because the grade could be a decimal.  eg: 87.3%

if (Grd >=0) and (Grd <=100):
    if (Grd >=80):
        print("You got an A")
    elif (Grd >=70):
        print("You got a B")
    elif (Grd >=60):
        print("You got a C")
    elif (Grd >=50):
        print("You got a D")
    elif (Grd >50):
        print("You got a D")
else:
    print("Your grade is invalid")

