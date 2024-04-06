from data_createData import create_data as cd
from data_retrieveData import retrieve_data as rd
from data_displayAllData import display_data as dd

class User:
    
    def __init__(self, name, address):
        self.name = name
        self.__address = address
        self.__books = {}

    def addUser(name):

        response = rd("users", name)

        if response is not None:
            print(f"\nFound user '{name}' in our system!\n")
        else:
            cd("users",name)
            print(f"\nUser '{name}' added to database...\n")

    def getUserBooks(name):
        user = rd("users", name)
        user_id = int(user[0])

        response = rd("borrowed_books", user_id)


        if response is not None:
            return response
        
        else:
            print(f"Sorry, {name} doesn't have any borrowed books on file!")
            


    def getUserDetails(name):
        response = rd("users", name)
        if response is not None:
            info = f"Name: {response[1]}, Address: {response[2]}"
            return info

        else:
            print(f"Sorry! I couldn't find a user named '{name}'")

    def displayAllUsers():
        response = dd("users")
        userList = []
        if isinstance(response, list):
            for user in response:
                info = f"Name: {user[1]}, Address: {user[2]}"
                userList.append(info)
            return userList
        else:
            for user in response:
                info = f"Name: {response[1]}, Address: {response[2]}"
                userList.append(info)
            return userList
