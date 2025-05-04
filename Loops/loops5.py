#Find The First Non_Repeated Character
word = input("Enter a word")
for X in word:
    if word.count(X)==0:    #.count() is a method used to count how many times a specific substring appears in the string.
   
        print(X)
        break  