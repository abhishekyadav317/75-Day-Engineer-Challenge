# progeram to search number ina given list

numbers = [ 4 , 7 , 2 , 9 ]
target = 10
found = False

for number in numbers :
    if target == number :
        found = True

if found == True :
    print ("Found")
else : 
    print("Not found")

