# 3. Attempt problem 1 using while loop.
#  Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter your number: "))
i = 1
for i in range(1,11):
    print(f"{number}x{i} = {number*i}")
    i += 1