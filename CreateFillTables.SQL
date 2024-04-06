-- SQL COMMANDS TO BUILD TABLES


CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(50)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre_id INT,
    isbn VARCHAR(30) NOT NULL,
    availability BOOLEAN DEFAULT True,
    quantity INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);


CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);


-- SQL COMMANDS TO FILL TABLE WITH DEFAULT DATA

INSERT INTO authors (name, biography)
VALUES ("JK Rowling","Author of the world famous Harry Potter series.."),
    ("Robert Louis Stevenson", "19th century author, famous for writing the novel 'Treasure Island'"),
    ("George Orwell","Mid 20th century novelist, famous for writing '1984', 'Animal Farm', 'Down and out in Paris and London', etc.");

INSERT INTO genres (name, description, category)
VALUES ("Fantasy", "Strange new worlds, magic spells, quests. Inner journeys manifested externally.","Fiction"),
        ("Science Fiction", "Brain Boggling books about the near to distant future. Often with dystopian or tragic themes.", "Fiction"),
        ("Horror", "Scary books about ghosts, murderers and other spooky subjects!", "Fiction"),
        ("Romance", "Romantic books about love, unrequited love, adventures, drama, etc", "Fiction"),
        ("Mystery", "Mysterious disappearances, disenchanted detectives, spiralling plots, crazy dames, etc", "Fiction");


INSERT INTO books (title, isbn, author_id, genre_id, availability, quantity)
VALUES ("1984", 124345436, 3, 2, True, 2),
        ("Treasure Island", 8049323, 2, 1, False, 0),
        ("Harry Potter", 9872343245, 1, 1, True, 10);

        


