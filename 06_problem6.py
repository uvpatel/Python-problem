'''6. Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F'''

marksa= float(input("Enter your marks: "))
marksb= float(input("Enter your marks: "))
marksc= float(input("Enter your marks: "))

per =( marksa+marksb+marksc)/3
print("Your persentage is:",per)

if(100>=per>=90):
    print("Your grade is Excellent ")
elif(90>per>=80):
    print("Your grade is A ")
elif(80>per>=70):
    print("Your grade is B ")
elif(70>per>60):
    print("Your grade is  C")
elif(60>per>50):
    print("Your grade is  D")
elif(50<per):
    print("Your grade is f ")
else:
    print("someyhing went wrong")