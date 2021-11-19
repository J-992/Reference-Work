#jaffer Razavi
#oct 9 2019

my_string = ("Hello World")

my_string.isalnum()		#check if all char are numbers
my_string.isalpha()		#check if all char in the string are alphabetic
my_string.isdigit()		#test if string contains digits
my_string.istitle()		#test if string contains title words
my_string.isupper()		#test if string contains upper case
my_string.islower()		#test if string contains lower case
my_string.isspace()		#test if string contains spaces
my_string.endswith('d')		#test if string endswith a d
my_string.startswith('H')	#test if string startswith H


print (my_string.isalnum())		#False
print (my_string.isalpha())		#False
print (my_string.isdigit())		#False
print (my_string.istitle())		#True
print (my_string.isupper())		#False
print (my_string.islower())		#False
print (my_string.isspace())		#False
print (my_string.endswith('d'))		#True
print (my_string.startswith('H'))		#True
