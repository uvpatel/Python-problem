a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
d = int(input("Enter your number: "))


if(a >b and a>c and a>d):
    print("a is gretest")

elif(b >c and b>a and b>d):
    print("b is gretest") 
elif(c > a and c> b and c>d):
    print("c  is gretest") 
elif(d > a and d> b and d>c):
    print("d  is gretest") 
# elif(a and b > c,a and b > d ):
#     print("a and b is gretest")
# elif(b and c > a,b and c > d ):
#     print("c and b is gretest")
# elif(a and c > b,a and c > d ):
#     print("a and c is gretest")
# elif(a and d > c,a and d > b ):
#     print("a and d is gretest")
# elif(b and d > c,b and d > a ):
#     print("b and d is gretest")
# elif(c and d > b,c and d > a ):
#     print("c and d is gretest")
# elif(c and b > a,b and c > d ):
#     print("c and b is gretest")

elif(a==b and b==c and c==a and a == d):
    print("a and b and c and d is greatest and equal")

else:
    print("Something went wrong")