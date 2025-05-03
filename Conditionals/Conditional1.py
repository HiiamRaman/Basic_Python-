1#Age Group Categorization
age = input("Write Your Age")  
integer_age = int(age) 

if(integer_age < 13):
    print("your are child")
    
elif(integer_age > 13 and integer_age < 20):
    print("your are Teenager") 
elif(integer_age > 20 and integer_age < 60):
    print("YOu are Adult")
else:
    print("You are superSenior")
    