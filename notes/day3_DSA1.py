# Program for finding smallest number in given list.
# Author : Abhishek Yadav 
# Date : 9/7/2026

numbers = [ 18 , 45 , 12 , 67 , 34 ]

smallest_number = numbers[0]

for number in numbers:
    if number < smallest_number :
        smallest_number = number

print(smallest_number) 