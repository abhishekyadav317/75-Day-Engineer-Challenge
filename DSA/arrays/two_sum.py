numbers = [2, 7, 11, 15]
target = 9

i = 0


for i in range(0 , len(numbers) ):
    for j in range(i+1, len(numbers)):
        

        pair_sum = numbers[i] + numbers[j]
        

        if pair_sum == target :
            print(i,j)

