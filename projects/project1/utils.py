def validate_amount(amount):
    if amount > 0 :
        return True
    else :
        return False

def validate_category(category):
    if category == "" :
        return False
    else:
        return True

def validate_description(description):
    if description == "":
        return False
    else :
        return True

def validate_date(date):
    if date == "" :
        return False
    else :
        return True

def get_valid_input(prompt , validator , error_message):

    while True :
        value = input(prompt)
        if validator(value):
            return value
        else :
            print(error_message)    

def get_valid_amount(prompt , validator , error_message) :
    while True :
        try :
            value = float(input(prompt))
        except ValueError :
            print("Invalid Input")
            continue

        if validator(value):
            return value
        else :
            print(error_message)

def get_valid_integer(prompt , error_message) :
    while True:

        try : 
            value = int(input(prompt))
        except ValueError :
            print(error_message)
            continue

        return value

