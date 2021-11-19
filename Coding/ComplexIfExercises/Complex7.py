#Jaffer Razavi
#oct 7 2019

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
