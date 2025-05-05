#lets grab knowledge about closure

# In Python, functions are just objects — like strings or numbers. You can:

# Assign them to variables

# Pass them as arguments

# Return them from other functions


def func1():
    X=50
    def func2():
        
      print(X)
    return func2     # here it just return func2
result = func1()
result()

 #Another Exmaple
def chai_code(num):
     def actual(x):
         return x ** num
     return actual
f = chai_code(2)
g =chai_code(3)
print(f(3))
print(g(3))