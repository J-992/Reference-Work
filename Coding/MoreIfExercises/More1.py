#jaffer Razavi
#Oct 9 2019
Weight = ' '
Height = ' '

Weight = float(input("what is your weight in kilograms? \n"))
Height = float(input("what is your height in metres? \n"))

Bmi = Weight/Height

if (Bmi >=0):
    if (Bmi >25):
        print("Your BMI is",round(Bmi,2),'. You are at risk of being overweight')
    elif (Bmi >=18.5) and (Bmi <=25):
        print("Your BMI is",round(Bmi,2),'. It is OK"')
    elif (Bmi <18.5):
        print("Your BMI is",round(Bmi,2),'. You may be underweight')
