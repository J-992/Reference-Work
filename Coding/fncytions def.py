# Jaffer Razavi
# Nov 21 2019
# Playing with subroutines



def roman():
    Num = int(input("Enter a number BETWEEN 1 and 10 \n"))

    if (Num >=1) or (Num <= 10):
        if (Num ==1):
            print("Your number in roman numerals is I")
        elif (Num ==2):
            print("Your number in roman numerals is II")
        elif (Num ==3):
            print("Your number in roman numerals is III")
        elif (Num ==4):
            print("Your number in roman numerals is IV")
        elif (Num ==5):
            print("Your number in roman numerals is V")
        elif (Num ==6):
            print("Your number in roman numerals is VI")
        elif (Num ==7):
            print("Your number in roman numerals is VII")
        elif (Num ==8):
            print("Your number in roman numerals is VIII")
        elif (Num ==9):
            print("Your number in roman numerals is IX")
        elif (Num ==10):
            print("Your number in roman numerals is X")
        else:
            print("ERROR: INVALID NUMBER")

    

def weight():
    Weight = float(input("What is the patients weight? \n"))
    if (Weight < 10):
        print("the dosage is", Weight*0.5,'mg')
    elif (Weight >=10) and (Weight <= 20):
        print("the dosage is", Weight*0.7,'mg')
    elif (Weight >=21) and (Weight <= 40):
        print("the dosage is", Weight*0.85,'mg')
    elif (Weight >41) and(Weight <= 70):
        print("the dosage is", Weight*1.1,'mg')
    elif (Weight >70):
        print("the dosage is", Weight*1.12,'mg')

#=======================================================================================================================================================================================



bob = input("""
Would you like to convert numbers to roman numerals or (type
roman) or would you like to calculate medication dosage? (type med)
\n""")

bob = bob.lower()

if bob == "med":
    weight()
elif bob == "roman":
    roman()






