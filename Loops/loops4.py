#Reverse a string
# string[start:stop:step]
# Breakdown of original_string[::-1]:
# start: omitted (means start from the end since step is negative)

# stop: omitted (means go until the beginning)

# step: -1 (means go backwards one step at a time)

word = input("enter a word")
rev_word = word[::-1]      #-1 (means go backwards one step at a time)
print(rev_word)
   