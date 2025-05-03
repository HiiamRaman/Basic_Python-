#Determinig if the food is Ripe ,OverRipe or unripe baseed on colors
color = input("Enter Fruit Color")

if(color.lower() == "green"):  #.lower() just conver user text into into lower case
    print("fruit is Unripe")
elif(color.lower() == "yellow"):
    print("Fruit is Ripe")
elif(color.lower() == "brown"):
    print("Fruit is OverRipe")
else:
    print("fruit is fresh")
    
    
    #Another Way
    # Determining if the food is Ripe, Overripe, or Unripe based on color
# color = input("Enter fruit color: ")

# Convert input to lowercase once to avoid repeating `.lower()`
# color = color.lower()

# if color == "green":
#     print("Fruit is unripe")
# elif color == "yellow":
#     print("Fruit is ripe")
# elif color == "brown":
#     print("Fruit is overripe")
# else:
#     print("Fruit is fresh")
