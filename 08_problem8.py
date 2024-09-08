# 8. Write a python function to print multiplication table of a given number

def table():
    n = int(input("Enter your number: "))
    i = 1
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
        i +=1
table()        
