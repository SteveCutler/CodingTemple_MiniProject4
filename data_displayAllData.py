from data_connectDatabase import connect_database
from mysql.connector import Error

def display_data(type, data = "*"):
         
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            try:
                query = f"SELECT {data} FROM {type}"
                cursor.execute(query)
                response = cursor.fetchall()
                return response
   
            except Error as e:
                print(f"\nChecking... This {type} is not already in our system.\n")
                return None

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()