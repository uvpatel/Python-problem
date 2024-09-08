# 10. Write a program to print multiplication table of n using for loops in reversed order.

number = int(input("Enter a number: "))
i = 10
while(i>=1):
    print(f"{number}X{i} =",number*i)
    i -=1