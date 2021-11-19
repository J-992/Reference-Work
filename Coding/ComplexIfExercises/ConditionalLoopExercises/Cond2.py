"""
Jaffer Razavi
Oct 24, 2019
Mean code that doesnt say hi to your name :(
"""

Name = ' '
MyName = "jaffer"

Name = input("What is your name? \n")
Name = Name.lower()

while (Name != MyName):
    Name = input("What is your name? \n")
    Name = Name.lower()

print("No, I am a mean program and I do not like you")

