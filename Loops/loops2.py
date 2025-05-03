#Calculate sum of Even Numbers up to N
number = input("Enter Your Number")  
entered_number = int(number)
sum = 0
for i in range(1,entered_number+1):   # here 1 is accepted and entered_number is not accepted.
    if(i%2==0):
        sum = sum+i
print(sum)