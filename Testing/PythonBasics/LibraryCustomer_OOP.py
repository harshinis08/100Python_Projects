class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def dispplayListOfAvailableBooks(self):
        print()
        print("List of available books: ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, book is not available in the list!")

    def returnedBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("Your book is successfully returned.")


class Customer:
    def requestBook(self):
        print("Enter the name of the book you want to borrow:")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you want to return:")
        self.book = input()
        return self.book


library = Library(['The Lord of the Rings', 'Harry Potter', 'The Alchemist', 'The Twilight Saga', 'The Da Vinci Code', 'Think and Grow Rich'])
customer = Customer()

while True:
    print("")
    print("Enter 1 to display the available books.")
    print("Enter 2 to to request for a book.")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    user_Choice = int(input())

    if user_Choice == 1:
        library.dispplayListOfAvailableBooks()
    elif user_Choice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif user_Choice == 3:
        returnedBook = customer.returnBook()
        library.returnedBook(returnedBook)
    else:
        quit()