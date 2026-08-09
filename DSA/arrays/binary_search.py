# divide search space O(logn)

'''
START

1. Take a sorted list and target.
2. Set left = 0.
3. Set right = len(list) - 1.
4. While left <= right:
      a. Calculate middle.
      b. If numbers[middle] == target:
             return middle.
      c. If numbers[middle] < target:
             move left to middle + 1.
      d. Otherwise:
             move right to middle - 1.
5. If the loop finishes, return -1.

END

Time Complexity: O(log n)
Space Complexity: O(1)
'''




def binary_search(numbers , target) : 
    left = 0
    right = len(numbers) - 1

    while left <= right :

        middle = (left + right)//2

        if numbers[middle] == target :
            return middle

        if numbers[middle] < target :
            left = middle + 1 
        else :
            right = middle - 1

    if numbers[middle] != target :
        return -1

print(binary_search([2, 4, 6, 8, 10, 12, 14], 12))