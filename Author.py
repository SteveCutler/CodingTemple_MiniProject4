from data_retrieveData import retrieve_data as rd
from data_createData import create_data as cd
from data_displayAllData import display_data as dd
class Author:
    def __init__(self, name, bio):
        self.name = name
        self.__bio = bio

    def addAuthor(name):

        response = rd("authors", name)


        if response is not None:
            #print(f"'{name}' is already in our authors database!\n")
            pass

        else:
            #call createData function to add author to the table
            cd("authors", name)

            print(f"\nAuthor '{name}' added to database!")

        

    def getAuthorDetails(name):
        response = rd("authors", name)
        if response is not None:
            info = f"Name: {response[1]}, Biography: {response[2]}"
            return info

        else:
            print(f"Sorry! I couldn't find a user named '{name}'")

    def booksByAuthor(name):
        authorID = rd("authors", name)
        if authorID is None:
            return None
        id = authorID[0]
        response = rd("booksByAuthorID",id)
        bookList = []
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
            print(f"Sorry! I couldn't find any books by the author '{name}'...")
            return None


    def displayAllAuthors():
        response = dd("authors")
        authorList = []
        if isinstance(response, list):
            for author in response:
                info = f"Name: {author[1]}, Address: {author[2]}"
                authorList.append(info)
            return authorList
        else:
            for user in response:
                info = f"Name: {response[1]}, Address: {response[2]}"
                authorList.append(info)
            return authorList



