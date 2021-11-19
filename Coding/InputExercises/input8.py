#Jaffer Razavi
# Oct 1 2019
#Variables and Input Exercise


Sub = str(input("What subject did you get a test for? \n"))
Mark = float(input("What were the total number of marks on the test? \n"))
Grade = float(input("How many marks did you get on the test? \n"))

print("Subject:", Sub)
print("Total number of marks on the test:", (format(Mark,'0,.0f')))
print("Your test marks:", (format(Grade,'0,.0f')))
#this is float because the mark they got on the test
#might have been a decimal

print("You got",(round(Grade/Mark*100, 1)),'%')
#print("You got", (format(Grade/Mark*100,'0,.1f'))+'%')

