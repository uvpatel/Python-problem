# 3. Check that a tuple type cannot be changed in python.
marks = ()
m1= int(input("Enter marks: "))
marks.append(m1)
m2= int(input("Enter marks: "))
marks.append(m2)
m3= int(input("Enter marks: "))
marks.append(m3)
m4= int(input("Enter marks: "))
marks.append(m4)
print(marks)

# conclusion is tuples are imutable