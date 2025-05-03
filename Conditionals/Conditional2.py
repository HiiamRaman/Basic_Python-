#Movie Ticket Pricing
age = input("Enter your Age :")
day = input("write what day is today")

integer_age = int(age)
if (integer_age < 18):
   price =  12 
else:
    price =  8
    

if (day.lower() == "wednesday"):   #lower() convert uppercase letter to lowercase
   price = price - 2
    
    
print("Price is ",price)