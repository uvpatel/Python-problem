'''6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''
dict = {"Urvil": "python" , "Abhishekh": "php", "mihir": "Java", "ramani": "c"}
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
 