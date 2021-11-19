#Jaffer Razavi
# Oct 1 2019
#Variables and Input Exercise


Rate = float(input("What is the interest rate?(Convert to decimal form) \n"))
Principal = float(input("How much are you investing? \n"))
Time = float(input("how much time (in years) are you investing money for? \n"))

print("You would earn", (round(Principal*Rate*Time, 1)),"in", (round(Time, 0)), "years")
