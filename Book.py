from User import User
from data_retrieveData import retrieve_data as rd
from data_createData import create_data as cd
from data_updateData import update_data as ud
from data_displayAllData import display_data as dd
from data_deleteData import delete_data as deldat
from datetime import datetime
from datetime import timedelta

class Book:
    def __init__ (self, title, isbn, author, genre, available, quantity):
        self.title = title
        self.isbn = isbn #int
        self.author = author
        self.genre = genre
        self.available = available #int
        self.quantity = quantity #int

    def addBook(title):

        response = rd("books", title)

        if response is not None:
            print(response)
            
            id = int(response[0])
            quantity = int(response[-1])
            quantity = quantity + 1
            success = ud("books","quantity",id,quantity)
            if success:
                print(f"\nFound {title} in our system... adding 1 to quantity!\n")
            else:
                print("Something went wrong...")

        else:
            cd("books", title)
            print(f"\nNew book '{title}' added to the database!\n")


    def borrowBook(user, book):
        
        response = rd("books", book)
        if response is not None:
            
            book_id = int(response[0])
            user = rd("users", user)
            user_id = int(user[0])
            comboID = [user_id, book_id]

            quantity = int(response[-1])
            newquantity = quantity - 1
            today = datetime.today()
            duedate = today + timedelta(weeks = 2)
            duedatestr = duedate.strftime('%Y-%m-%d')

            if quantity > 1:

                create = cd("borrowed_books", comboID)
                print("creating record...")
                if create:
                    print("\nBook succesfully borrowed!")
                    print(f"Your book duedate is:{duedatestr}")
                    ud("books","quantity",book_id, newquantity)
            elif quantity == 1:
                
                create = cd("borrowed_books", comboID)
                if create:
                    print("\nBook succesfully borrowed!")
                    print(f"Your book duedate is:{duedatestr}")
                    ud("books","quantity",book_id, newquantity)
                    ud("books","availability",book_id, False)
            else:
                
                print("This book is unavailable due to lack of quantity!")
        else:
            print(f"This book is not in our system! Sorry")
        
    def returnBook(user, book):

        response = rd("books", book)
        quantity = response[-1]
        newquantity = quantity + 1

        book_id = int(response[0])
        response = rd("users", user)
        user_id = int(response[0])

        response = rd("borrowed_books", user_id)
        borrowed_id = False

        if isinstance(response,list):
            for entry in response:
                if int(entry[1]) == user_id and int(entry[2]) == book_id:
                    borrowed_id = entry[0]
        else:
            borrowed_id = response[0]
            


        if borrowed_id:

            if quantity == 0:
                ud("books","quantity",book_id, newquantity)
                
                ud("books","availability",book_id, True)
                
                deldat("borrowed_books", borrowed_id)
                print(f"{book} has been returned to the shelf...\n")
                print(f"{book} is now available to borrow again!\n")

            else:
                ud("books","quantity",book_id, newquantity)
                
                deldat("borrowed_books", borrowed_id)
                print(f"{book} has been returned to the shelf...\n")

        else:
            print(f"We couldn't find the book you're looking to return! Sorry")    


    def searchBook(title):
        response = rd("books", title)
        bookList = False
        if response is not None:
            if isinstance(response, list):
                for book in response:
                    info = f"Title: {book[1]}, Author: {rd("authorsbyid", book[2]) [0]}, Genre: {rd("genresbyid", book[3]) [0]}, ISBN: {book[4]}, Availability: {book[5]}, Quantity: {book[6]}"
                    bookList.append(info)
                return bookList

            else:
                info = f"Title: {response[1]}, Author: {rd("authorsbyid", response[2]) [0]}, Genre: {rd("genresbyid", response[3]) [0]}, ISBN: {response[4]}, Availability: {response[5]}, Quantity: {response[6]}"
                return info
        else:
            print(f"Sorry, we couldn't find a book titled '{title}'")

    def displayBooks():
        response = dd("books")
        bookList = []
        for book in response:
            info = f"Title: {book[1]}, Author: {rd("authorsbyid", book[2]) [0]}, Genre: {rd("genresbyid", book[3]) [0]} ISBN: {book[4]}, Availability: {book[5]}, Quantity: {book[6]}"
            bookList.append(info)
        return bookList
        
