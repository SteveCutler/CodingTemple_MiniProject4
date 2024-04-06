# Project Requirements


 
# Menu Actions:

#     Implement the following actions in response to menu selections using the classes you've created:

# - Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as "Borrowed."
# - Allowing users to return a book, marking it as "Available."
# - Searching for a book by its unique identifier (ISBN or title) and displaying its details.
# - Displaying a list of all books with their unique identifiers.
# - Adding a new user with user details.
# - Viewing user details.
# - Displaying a list of all users.
# - Adding a new author with author details.
# - Viewing author details.
# - Displaying a list of all authors.
# - Adding a new genre with genre details.
# - Viewing genre details.
# - Displaying a list of all genres.
# - Quitting the application.

#     Functions for Data Manipulation:

#     Create functions for adding new books, users, authors, and genres to the database.

#     Implement functions for updating book availability, marking books as borrowed or returned.

#     Develop functions for searching books by ISBN, title, author, or genre.

#     Define functions for displaying lists of books, users, authors, and genres.

#     Implement functions for user registration and viewing user details.

#     Follow PEP 8 style guidelines for code formatting and structure.

#     Ensure proper indentation and spacing for readability.

#     Effective Project Communication:
#     Create a video presentation or explanation of the Library Management System project.
#     Demonstrate the ability to explain technical concepts and project details in a concise and understandable manner.

#     Create seperate module for database operations





# In this project, you will integrate a MySQL database with Python to develop an advanced Library Management System. 
# This command-line-based application is designed to streamline the management of books and resources within a library. 
# Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of
# books while demonstrating your proficiency in database integration, SQL, and Python.

# Integration with the "Library Management System" Project from Module 4 (OOP):

# For this project, you will build upon the foundation laid in "Module 4: Python Object-Oriented Programming (OOP)." 
# The object-oriented structure and classes you developed in that module will serve as the core framework for the Library 
# Management System. You will leverage the classes such as Book, User, Author, and Genre that you previously designed,
# extending their capabilities to integrate seamlessly with the MySQL database.

# Enhanced User Interface (UI) and Menu:

#     Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus 
# for each class of the system.

#     Welcome to the Library Management System with Database Integration!
#     ****
#     Main Menu:
#     1. Book Operations
#     2. User Operations
#     3. Author Operations
#     4. Genre Operations
#     5. Quit

#         Book Operations:

#         Book Operations:
#         1. Add a new book
#         2. Borrow a book
#         3. Return a book
#         4. Search for a book
#         5. Display all books

#         User Operations:

#         User Operations:
#         1. Add a new user
#         2. View user details
#         3. Display all users

#         Author Operations:

#         Author Operations:
#         1. Add a new author
#         2. View author details
#         3. Display all authors

#         Genre Operations:

#         Genre Operations:
#         1. Add a new genre
#         2. View genre details
#         3. Display all genres



# Database Integration with MySQL:

#     Integrate a MySQL database into the Library Management System to store and retrieve data related to books, users,
# authors, and genres.
#     Design and create the necessary database tables to represent these entities. You will align these tables with the 
# object-oriented structure from the previous project.
#     Establish connections between Python and the MySQL database for data manipulation, enhancing the persistence and 
# scalability of your Library Management System.

# Data Definition Language Scripts:

#     Create the necessary database tables for the Library Management System. For instance:

#     Books Table:

# CREATE TABLE books (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     author_id INT,
#     genre_id INT,
#     isbn VARCHAR(13) NOT NULL,
#     publication_date DATE,
#     availability BOOLEAN DEFAULT 1,
#     FOREIGN KEY (author_id) REFERENCES authors(id),
#     FOREIGN KEY (genre_id) REFERENCES genres(id)
# );

#     Authors Table:

# CREATE TABLE authors (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     biography TEXT
# );

#     Genres Table:

# CREATE TABLE genres (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     description TEXT,
#     category VARCHAR(50)
# );

#     Users Table:

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     library_id VARCHAR(10) NOT NULL UNIQUE
# );

#     Borrowed Books Table:

# CREATE TABLE borrowed_books (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT,
#     book_id INT,
#     borrow_date DATE NOT NULL,
#     return_date DATE,
#     FOREIGN KEY (user_id) REFERENCES users(id),
#     FOREIGN KEY (book_id) REFERENCES books(id)
# );

