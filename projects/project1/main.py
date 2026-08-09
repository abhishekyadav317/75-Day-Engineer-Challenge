from utils import validate_amount , validate_category , validate_description , validate_date , get_valid_input , get_valid_amount


print('''=======================
    EXPENSE TRACKER
=======================
''')


print("Application started successfully.")

amount = get_valid_amount(
    "Enter Amount : ",
    validate_amount,
    "Amount must be greater than zero"
)

category = get_valid_input(
    "Enter Category : " ,
    validate_category , 
    "Category must not be empty"
)

description = get_valid_input(
    "Enter Description : " , 
    validate_description ,
    "Description must not be empty"
)

date = get_valid_input(
    "Enter Date : " , 
    validate_date ,
    "Date must not be empty"
)



print("Expense Added Successfully!")

print("=======Expense=======")

print(f"Amount : {amount}")
print(f"Category : {category}")
print(f"Description : {description}")
print(f"Date : {date}")

print("=====================")



