# Code for finding largest number in a given list 
# Author : Abhishek 
# Date : 7/8/2026

numbers = []
largest_number = numbers[0] 

for number in numbers:
    if number > largest_number:
        largest_number = number
    
print(largest_number)