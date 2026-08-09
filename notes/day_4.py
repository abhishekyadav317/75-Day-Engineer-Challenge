# make function for calculate total

'''
def calculate_total ( a , b ) :
    total = a + b
    return total

calculate_total( 100 , 250 )

def is_even(number):
    if number % 2 == 0 :
        return True
    else :
        return False

def find_largest(a , b , c) :
    if a > b :
        if a > c :
            return a
        else :
            return c
    else :
        if b > c :
            return b
        else :
            return c

print(find_largest(5,5,5))
'''
expenses = [120.50, 50, 200, 75]


def calculate_expense_total(expenses):
    total = 0
    for expense in expenses :
        total = total + expense

    return total

print(calculate_expense_total(expenses))

    



