#Print the multiplicatiion of number up to 10 and skip iteration 5.

# number  = input("Enter your Number ")
# num = int(number)
# for i in range(1,5):
#     multiplication = num * i
#     print(multiplication)
    
# for i in range(6,11):
#     multiplication = num * i
#     print(multiplication)
   
#haha this was my logic but it can be improved 
number = input("Enter your number")
num = int(number)
for i in range(1,11):
    if(i==5):
      continue
    else:
      multiplication = num * i
      print(multiplication)