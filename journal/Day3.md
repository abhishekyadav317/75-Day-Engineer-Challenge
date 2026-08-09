# Day 3 DSA Algorithm Patterns

## Pattern 1: Counter Pattern

### Purpose

Use this pattern when we need to count how many elements satisfy a condition.

### Steps

1. Initialize `count = 0`.
2. Traverse every element in the list.
3. Check the required condition.
4. If the condition is true, increase the count by 1.
5. After checking all elements, print or return the final count.

### Examples

* Count even numbers
* Count odd numbers
* Count numbers greater than 50
* Count negative numbers
* Count students who passed

---

## Pattern 2: Accumulator Pattern

### Purpose

Use this pattern when we need to calculate a total by continuously adding values.

### Steps

1. Initialize `total = 0`.
2. Traverse every element in the list.
3. Add the current element to the total.
4. Update the total after every addition.
5. Print or return the final total.

### Examples

* Sum of numbers
* Average of numbers
* Total salary
* Total marks
* Total shopping bill

---

## Pattern 3: Best Value Pattern

### Purpose

Use this pattern when we need to find the best value in a collection, such as the largest or smallest element.

### Steps

1. Assume the first element is the best value.
2. Traverse the remaining elements.
3. Compare the current element with the current best value.
4. If the current element is better, update the best value.
5. After checking all elements, print or return the final best value.

### Examples

* Largest number
* Smallest number
* Highest salary
* Lowest temperature
* Maximum score

---

## Pattern 4: Flag Pattern

### Purpose

Use this pattern when we need to check whether a condition becomes true during processing.

### Steps

1. Initialize `found = False`.
2. Traverse every element in the list.
3. Check the required condition.
4. If the condition is true, set the flag to `True`.
5. After processing, use the flag to decide the final output.

### Examples

* Search for a number
* Check whether a username exists
* Check whether a product is available
* Check whether a student is present
* Verify whether a password is correct
