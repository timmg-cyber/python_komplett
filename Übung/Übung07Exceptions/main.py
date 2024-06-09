# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

## Aufgabenstellung:
# Sie sind für den Checkout-Prozess einer Bibliothek verantwortlich. Nutzen Sie die
# vorprogrammierten Exceptions um gewisse Fehler abzufangen und zu behandeln.
#
# Folgende Schritte sollen behandelt werden:
# - schreiben Sie die Methode check_out_book um ein Buch auzuleihen
# - updaten Sie den Status available im library dictionary wenn ein Buch ausgeliehen wird
# - behandeln Sie Fehlermeldungen, die hierbei auftreten können
##
class BookNotFoundException(Exception):
    pass

class BookNotAvailableException(Exception):
    pass

library = {
    "1984": {
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "genre": "Fiction",
        "available": False
    },
    "Pride and Prejudice": {
        "author": "Jane Austen",
        "genre": "Romance",
        "available": "False"
    },
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True
    },
    "The Catcher in the Rye": {
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "available": False
    }
}
def check_out_book(book):
    """This function should do a checkout process for a given book"""
    ## Ihr Code
    pass

def check_if_book_available(book):
    """This function checks whether a book is available or not"""
    ## Ihr Code
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book = "The Great Gatsby"
    check_out_book(book)
    book2 = "The Catcher in the Rye"
    check_out_book(book2)
    book3 = "Harry Potter and the Goblet of Fire"
    check_out_book(book3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
