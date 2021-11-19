#Jaffer Razavi
#Oct 2 2019

Age = ' '
Vote_Age = 18

Age = int(input("How old are you? \n"))

if (Age >= Vote_Age):
    print("OLD ENOUGH TO LEGALLY VOTE")
else:
    print("YOU ARE NOT OLD ENOUGH TO VOTE \n"
          "YOU HAVE", Vote_Age-Age, "YEARS LEFT UNTIL YOU CAN LEGALLY VOTE")
