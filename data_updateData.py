from data_connectDatabase import connect_database
from mysql.connector import Error

def update_data(type, column, id, newvalue):
         
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            try:
                query = f"UPDATE {type} SET {column} = {newvalue} WHERE id = {id}"
                cursor.execute(query)
                conn.commit()
                return True
            except Error as e:
                return False

        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            cursor.close()
            conn.close()