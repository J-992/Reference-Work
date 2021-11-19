'''
Jaffer Razavi
Oct 26, 2019
Inputting and outputting numbers.
'''

Num1 = 0
Num2 = 0


Num1 = float(input("Enter a number: \n"))
Num2 = float(input("Enter another number: \n"))

Ans = Num1*Num2

while (Ans >= 0):
    print(Num1,'x',Num2,'=',Ans)
    Num1 = float(input("Enter a number: \n"))
    Num2 = float(input("Enter another number: \n"))
    Ans = Num1*Num2

print(Num1,'x',Num2,'=',Ans)  #prints it again if the number is negative
