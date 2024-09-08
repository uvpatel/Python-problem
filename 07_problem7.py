# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

dict = {"Urvil": "python" , "Abhishekh": "php", "mihir": "Java", "Urvil": "c"}
name = input(f"Enter your name: ")
if(name=='Urvil'):
   print(f"Your language is: {dict['Urvil']}")
elif(name=='ramani'):
    print(f"Your language is: {dict['ramani']}")
elif(name=='Abhishekh'):
    print(f"Your language is: {dict['Abhishekh']}")
elif(name=='mihir'):
    print(f"Your language is: {dict['mihir']}")

else:
    print("Something went wrong") 

#  If name is similar so it gave output last initializing