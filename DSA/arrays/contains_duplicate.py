# Given an any integer array : numbers=[1,2,3,1]
# return True 

# Algorithm :
'''
1.start 
2.traverse each element in list 
3.for each element compare it with every alament after i
4.if two element are equal :
      return true
5.continue until all commparison are complemented 
6.if no duplicate is found:
    return false

'''

numbers = [1, 2, 3, 1]

found = False

for i in range(len(numbers)):

    for j in range(i+1 , len(numbers)) :

        if numbers[i] == numbers[j]:
            found = True
            break
            

print(found)








