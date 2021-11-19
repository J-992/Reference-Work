#jaffer Razavi
#oct 23 2019
#factorials part a

import math

Num = int(input("Enter a number that you want a factorial of \n"))
Fact = 1
  
for i in range(1,Num+1): 
    Fact = Fact * i 
      
print ("The factorial of",Num," is", Fact) 


