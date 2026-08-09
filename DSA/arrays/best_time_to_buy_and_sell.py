#Best Time to Buy and Sell Stock
'''
START

1. Take the list of daily stock prices.
2. Assume the first price is the lowest price seen so far.
3. Initialize maximum profit as 0.
4. Traverse the list from left to right.
5. If the current price is lower than the lowest price, update the lowest price.
6. Otherwise, calculate the profit by subtracting the lowest price from the current price.
7. If this profit is greater than the maximum profit, update the maximum profit.
8. After checking all prices, return the maximum profit.

END

'''


prices = [ 7, 6, 5, 4, 3 ]

lowest_price = prices[0]

maximum_profit = 0

for price in prices :

    if price < lowest_price :
        lowest_price = price 
    
    profit = price - lowest_price

    if profit > maximum_profit :
        maximum_profit = profit

print(maximum_profit)



