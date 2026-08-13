from database import get_connection


def save_expense(amount , category , description , date ) :
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        INSERT INTO expenses (amount , category , description , date )
        VALUES (?,?,?,?)  ''' , 
        ( amount , category , description , date )
    )

    connection.commit()
    connection.close()

def get_all_expenses():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT id , amount, category , description , date
        FROM expenses;
        '''
    )
    rows = cursor.fetchall()
    connection.close()
    return rows


def update_expense_amount(expense_id , new_amount) :
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        UPDATE expenses 
        SET amount = ?
        WHERE id = ?
        ''',
        (new_amount,expense_id)
    )
    affected_rows = cursor.rowcount
    connection.commit()
    connection.close()
    return affected_rows


def delete_expense(expense_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        DELETE FROM expenses
        WHERE id = ?
        ''',
        (expense_id,)
    )
    affected_rows = cursor.rowcount
    connection.commit()
    connection.close()
    return affected_rows