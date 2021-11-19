#Jaffer Razavi
#October 2, 2019
#Simple If structures question 2

Num1 = ' '
Num2 = ' '
Ans = ' '



Num1 = int(input("What is your first number? (Cannot be a decimal) \n"))
Num2 = int(input("What is your second number? (Also cannot be a decimal) \n"))

Cor_Ans = int(Num1+Num2)

print("What is the answer to the equation: \n", Num1, '+', Num2, '= ??')
Ans = int(input("Answer? \n")) 

if(Ans == Cor_Ans):
    print("Good job, your answer is correct!")

else:
    print("Wrong! \n bye!")
    quit()

