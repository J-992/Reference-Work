'''
Jaffer Razavi
Oct 28, 2018
Input word number, prints word number of times.
'''

Word = input("Enter a word \n")
Num = int(input("Enter a number \n"))

while Num != 0:
    for i in range (Num):
        print(Word, end=' ')
    Num = int(input("\n Enter a number \n"))
