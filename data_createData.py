from data_connectDatabase import connect_database
from data_retrieveData import retrieve_data
from mysql.connector import Error
from datetime import datetime
from datetime import timedelta




def create_data(type, name):

    if type == "authors":
        
        columns = "(name, biography)"
        bio = input("Please enter a one sentence bio for the author:\n").strip().capitalize()
        vars = [name, bio]

    if type == "books":
        from Author import Author
        from Genre import Genre

        columns = "(title, isbn, author_id, genre_id, availability, quantity)"
        isbn = input("What is the ISBN number of your book?\n").strip()
        try:
            isbn = int(isbn)
        except Error as e:
            print(f"The values '{isbn}' isn't a valid integer, please try again!")

        author = input(f"Who is the author of {name}?\n").strip().lower().title()

        Author.addAuthor(author)
        author_id = retrieve_data("authors", author, "id")
        author_id = int(author_id[0])
        
        print("Here are all the genres in our system:\n")
        genreList = Genre.displayAllGenres()
        
        for genre in genreList:
            print(genre)

        genre = input("\nWhich is the genre of your book? select from the list - or enter your own to create a new one\n").strip().lower().title()
        Genre.addNew(genre)
        genre_id = retrieve_data("genres", genre, "id")
        genre_id = int(genre_id[0])
        vars = [name, isbn, author_id, genre_id, True, 1]

    if type == "genres":
        
        from Genre import Genre
        columns = "(name, description, category)"
        description = input(f"\nPlease enter a one sentence description of the Genre '{name}':\n")
        category = input(f"\nWhat category of book is this? (Fiction, Non-fiction)").strip().title()
        vars = [name, description, category]

    if type == "users":
        
        columns = "(name, address)"
        print(f"Lets register user '{name}' so you can borrow books..\n")
        address = input(f"What address would you like to put on file for {name}\n").strip().lower().title()
        vars = [name, address]

    if type == "borrowed_books":

        columns = "(user_id, book_id, borrow_date, return_date)"
        today = datetime.today()
        todaystr = today.strftime('%Y-%m-%d')
        duedate = today + timedelta(weeks = 2)
        duedatestr = duedate.strftime('%Y-%m-%d')
        user_id, book_id = name
        vars = [user_id, book_id, todaystr, duedatestr]

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            vars = tuple(vars)
            query = f"INSERT INTO {type} {columns} VALUES {vars}"

            cursor.execute(query)
            conn.commit()
            return True

        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            cursor.close()
            conn.close()