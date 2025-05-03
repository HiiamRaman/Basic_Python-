#Grade of student
Marks = input("Enter Student Marks")
integer_Marks = int(Marks)
if(integer_Marks >= 90 and integer_Marks <= 100):
    print("A-grade")
elif(integer_Marks >= 80 and integer_Marks <= 89):
    print("B-grade")
elif(integer_Marks >= 70 and integer_Marks <= 79):
    print("C-grade")
elif(integer_Marks >= 60 and integer_Marks <= 69):
    print("D-grade")
else:
    print("Fail")
    