#jaffer Razavi
#oct 21, 2019
#list input then get averages of input

avg=0.0

for i in range(4):  #prints the statement 4 times
    try:
        avg = avg + float(input("Please input number " + str(i+1) + " "))
    except ValueError:
        print("Invalid Input")  #if the incorrect input is inputted, this will happen
        
print("The average is " + str(avg/4))


# this helped:
#https://stackoverflow.com/questions/40404093/how-to-use-a-for-loop-with-input-function

