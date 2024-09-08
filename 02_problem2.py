# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

greet = "good morning"

# name = str(input("Enter your name: "))
i = 0
for name in l :
    print(f"{l[i]}, {greet}")
    i +=1