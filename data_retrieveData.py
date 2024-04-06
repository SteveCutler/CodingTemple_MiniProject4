from data_connectDatabase import connect_database
from mysql.connector import Error

def retrieve_data(type, label, data = "*"):
         
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            try:
                if type == "books":
                    query = f"SELECT {data} FROM {type} WHERE title = '{label}'"

                elif type == "borrowed_books":
                    query = f"SELECT {data} FROM {type} WHERE user_id = '{label}'"

                elif type == "titlefromid":
                    query = f"SELECT title FROM books WHERE id = '{label}'"
                
                elif type == "authorsbyid":
                    query = f"SELECT name FROM authors WHERE id = '{label}'"

                elif type == "booksByAuthorID":
                    query = f"SELECT * FROM books WHERE author_id = '{label}'"

                elif type == "booksByGenreID":
                    query = f"SELECT * FROM books WHERE genre_id = '{label}'"

                elif type == "genresbyid":
                    query = f"SELECT name FROM genres WHERE id = '{label}'"
                    
                else:
                    query = f"SELECT {data} FROM {type} WHERE name = '{label}'"

                cursor.execute(query)
                response = cursor.fetchall()

                if response:
                    if len(response) == 1:
                        return response[0]
                    else:
                        return response
                else:
                    return None
                
            except Error as e:
                print(f"\nChecking... '{label}' is not in our system.\n")
                return None

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            cursor.close()
            conn.close()