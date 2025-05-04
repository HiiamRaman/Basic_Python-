#Polymorphism in Function
# In Python, polymorphism in functions refers to the ability to use the same function name to do different things
def Add(a,b):
    return (a+b)
result  = Add(2,3)
print("final result is ",result)
#Lets try ton use the function on different  things
print(Add("Raman","Singh")) # Here we Added two strings
print (Add([1,2],[3]))  