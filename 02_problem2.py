'''2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
'''

phy_marks = float(input("Enter marks: "))
chem_marks = float(input("Enter marks: "))
maths_marks = float(input("Enter marks: "))

per = (phy_marks+chem_marks+maths_marks)/3

print(per)
if(per<40):
    print("You are fail")

elif(phy_marks<33 and chem_marks<33 and maths_marks<33):
    print("Your one subject marks is not sufficient,so u are")    