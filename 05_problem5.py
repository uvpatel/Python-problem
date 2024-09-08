# 5. Write a program which finds out whether a given name is present in a  or not.

l= [ "Urvil" , "abhi" , "hiten" ,"ramani" ,"krish"]

name = input("Enter your name: ")

if(name  in l ):
    print(f"This  is talking about {name}")
# elif("hiten" in l ):
#     print("This  is talking about hiten")
# elif("abhi" in l):
#     print("This  is talking about abhi")
# elif("ramani" in l ):
#     print("This  is talking about ramani")
else:
    print("The candidate isn't in list")