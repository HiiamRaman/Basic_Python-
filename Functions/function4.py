#Function Returing Single Values
def Sum(a,b):
   return a+b
result = Sum(2,3)
print("first result is",result)
def Sub(result,c):
       return result-c
new_result = Sub(result,10)
print("after Subtration",new_result)


#Function returning multiple values
def Sum(a,b):
    return a+b,a-b
result = Sum(5,5)    #Here the result will be stored like (10,0)   so X,Y = (10,0)
X,Y= result
print("Sum of them is",X)
print("Difference of them is",Y)
