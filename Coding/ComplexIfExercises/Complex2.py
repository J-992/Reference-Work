#Jaffer Razavi
#Oct 4 2019


Price = float(input("What was the purchase price of the item? (In $) \n"))
Prov = input("What province was your item purchased in? (CASE SENSITIVE) \n")

if (Prov == 'Nunavut') or (Prov == 'Northwest Territories') or (Prov == 'Alberta') or (Prov == 'Yukon'):
    print("The sales tax in on your item is", '$',round(Price*0.05,2))
elif(Prov == 'Newfoundland and Labrador') or (Prov == 'Prince Edward Island') or (Prov == 'PEI') or (Prov == 'Nova Scotia') or (Prov =='New Brunswick'):
    print("The sales tax in on your item is", '$',round(Price*0.15,2))
elif(Prov == 'Quebec'):
    print("The sales tax in on your item is", '$',round(Price*0.14975,2))
elif(Prov == 'Ontario') or (Prov =='Manitoba'):
    print("The sales tax in on your item is", '$',round(Price*0.13,2))
elif(Prov == 'Saskatchewan'):
    print("The sales tax in on your item is", '$',round(Price*0.11,2))
elif(Prov == 'British Columbia'):
    print("The sales tax in on your item is", '$',round(Price*0.12,2))
else:
    print("Is that a province? if it is, please capitalize the first letter.")


    
          
 
