'''4. Write a program to find whether a given username contains less than 10
characters or not.'''

user_name = input("Enter your name: ")
if(len(user_name)>10):
    print("Given name contain more than 10 letters")
elif(len(user_name)<=10):
    print("Given name contain less than 10 letters")
    
else:
    print("something went wrong")    