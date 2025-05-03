tea_types = ("black","Green", "Blue","Oolong")
print (tea_types)


print(tea_types[0])

print (tea_types[2])
print(tea_types[0:])  #Slicing
more_tea = ("Black_Herbal" , "Green_Herbal", "Masala_herbal")
another_tea = ("blue", "green","yellow")
all_tea = more_tea + another_tea 
print(all_tea)

if "Black_Herbal" in all_tea :
    print("we have this Type of tea")