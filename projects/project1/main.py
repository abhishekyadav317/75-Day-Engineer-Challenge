from utils import validate_amount , validate_category , validate_description , validate_date , get_valid_input , get_valid_amount , get_valid_integer
from database import initialize_database
from storage import save_expense, get_all_expenses , update_expense_amount , delete_expense



# ADD Expense Amount :

def add_expense():
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
    save_expense(amount,category,description,date)
    print("Expense Added Successfully!")

# View Expenses     

def view_expenses():
    expenses = get_all_expenses()

    for expense in expenses :
        expense_id , amount , category , description , date = expense
        print("ID : ",expense_id)
        print(f"Amount : ₹{amount:.2f}")
        print("Category : ",category)
        print("Description : ",description)
        print("Date : ",date)
        print("============================")



def main() :
    print('''=======================
    EXPENSE TRACKER
=======================
    ''')
    print("Application started successfully.")
    initialize_database()
    while True :

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense Amount")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1" :
            add_expense()



        elif choice == "2" :
            view_expenses()



        elif choice == "3" :

            expense_id = get_valid_integer(
                "Enter Expense ID : ",
                "Expense ID must be an integer"
            )
            new_amount = get_valid_amount(
                "Enter New Amount : ",
                validate_amount ,
                "Amount must be greater than zero "
            )

            affected_rows = update_expense_amount(expense_id , new_amount)
            if affected_rows == 1 :
                print("Successfully updated expense")
            else :
                print("Expense ID not found")

        elif choice == "4" :

            expense_id = get_valid_integer(
                "Enter Expense ID : ",
                "Expense ID must be an  integer"
            )
            affected_rows = delete_expense(expense_id)
            if affected_rows == 1 :
                print("Expense deleted successfully")
            else :
                print("Expense ID not found")


        elif choice == "5" :
            print("GoodBYE!")
            break
        else :
            print("Invalid Choice")



if __name__ == "__main__" :
    main()






