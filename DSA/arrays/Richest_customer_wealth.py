accounts = [
    [ 1 , 5 ] ,
    [ 7 , 3 ] ,
    [ 3 , 5]
]

richest_wealth = 0

for customer in accounts:
    customer_total = 0

    for account in customer:
        customer_total = customer_total + account

    if customer_total > richest_wealth :
        richest_wealth = customer_total

print(richest_wealth)






