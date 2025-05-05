
# username = "Raman"
# def func1 ():
#    username = "Binay"
#    print (username)   #This print Binay
   
#    def func2():
#        print ("Billa")
      
#    func2()
# func1()
# print(username) #Tphis Prints Raman

    #For better understanding  
    
username = "Raman"

def func1():
    username = "Binay"
    print(username)   # This prints "Binay"
    
    def func2():
        print("Billa")  # This will be printed when func2 is called

    func2()  # Now func2 is called here

func1()
print(username)  # This prints "Raman"
