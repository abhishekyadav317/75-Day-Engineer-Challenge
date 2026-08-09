# program to find average of all numbers present in list 

numbers = [ 10 , 20 , 30 ]

total = 0 

for number in numbers :
    total = total + number
    
average = total / len(numbers)

print(average)