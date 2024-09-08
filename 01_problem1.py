# 1. Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter a number: "))
i = 1
while(i<11):
    print(f"{number}X{i} =",number*i)
    i += 1 