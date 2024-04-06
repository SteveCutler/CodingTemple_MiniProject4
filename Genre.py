
# from Book import LibraryBooks
from data_retrieveData import retrieve_data as rd
from data_displayAllData import display_data as dd
from data_createData import create_data as cd

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.__description = description
        self.category = category
    
    def addNew(name):

        response = rd("genres", name)

        if response is not None:
            print(f"\nSorry, the genre {name} already exists in our system!\n")

        else:
            print(f"\nWe couldn't find '{name}' in Genres list, lets add it...\n")
            cd("genres", name)
            print(f"\nGenre '{name}' added succesfully!\n")

    
    def getGenreDetails(genre):
        response = rd("genres", genre)
        if response is not None:
            info = f"Name: {response[1]}, Description: {response[2]}, Category: {response[3]}"
            return info

        else:
            print(f"Sorry! I couldn't find a genre named '{genre}'")

        
    def viewGenreBooks(genre):
        genreID = rd("genres", genre)
        if genreID is None:
            return None
        id = genreID[0]
        response = rd("booksByGenreID",id)
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
            print(f"Sorry! I couldn't find any books under the genre '{genre}'...")
            return None

    
    def displayAllGenres():

        response = dd("genres")
        if response is not None:
            genreList = []
            for genre in response:
                info = f" - {genre[1]}"
                genreList.append(info)
            return genreList
        else:
            print("Sorry, couldn't find that!")


    
Genres = {"Fantasy": Genre("Fantasy", "Strange new worlds, magic spells, quests. Inner journeys manifested externally.","Fiction"), "Science Fiction": Genre("Science Fiction", "Brain Boggling books about the near to distant future. Often with dystopian or tragic themes.", "Fiction"), "Horror": Genre("Horror", "Scary books about ghosts, murderers and other spooky subjects!", "Fiction"), "Romance": Genre("Romance", "Romantic books about love, unrequited love, adventures, drama, etc", "Fiction"), "Mystery": Genre("Mystery", "Mysterious disappearances, disenchanted detectives, spiralling plots, crazy dames, etc", "Fiction")}