#Check whether a number is positive, negative, or zero.
'''
number = float(input("Enter number to check it is positive , negative , or zero : "))

if number > 0 :
    print("Number is Positive")
elif number < 0 :
    print("Number is Negative")
else : 
    print("Number is zero")
'''

#Check whether a year is a leap year (hint: use % and if-elif-else).
'''
year = int(input("Enter year to check it is leap year or not : "))

if year % 400 == 0 :
    print(f"{year} is leap year")
elif year % 4 == 0 :
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

'''    

# Build a simple login system with a username and password.
'''
username = "Abhi"
password = "pass1122"

enter_username = input("Enter username : ")
enter_password = input("Enter password : ")

if username == enter_username :
    if password == enter_password :
        print("you have succesfully login!")
    else : 
        print("invalid password!")
else:
    print("Invalid credential!")
'''

#Input three numbers and print the largest.

'''
number_1 = float(input("Enter number 1 : "))
number_2 = float(input("Enter number 2 : "))
number_3 = float(input("Enter number 3 : "))

if number_1 > number_2 :
    if number_1 > number_3 :
        print(f"{number_1}")
    else:
        print(f"{number_3}")
else :
    if number_2 > number_3 :
        print(f"{number_2}")
    else :
        print(f"{number_3}")

'''

#Input marks and print grades: A, B, C, D, or F.
'''
marks = int(input("Enter your marks : "))

if marks >= 90 :
    print("your grade is A")
elif marks >= 75 :
    print("Your grade is B")
elif marks >= 60 :
    print("Your grade is C")
elif marks >= 45 :
    print("Your grade is D")
else :
    print("Your grade is F")

'''


