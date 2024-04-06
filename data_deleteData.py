from data_connectDatabase import connect_database
from mysql.connector import Error

def delete_data(table, id):
         
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            try:
                query = f"DELETE FROM {table} WHERE id = {id}"
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