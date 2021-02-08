import sys
class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayAvailableBooks(self):
        print("The books we have in our library are as follows:")
        print("================================")
        for book in self.availablebooks:
            print(book)

    def lendBook(self, requestedbook):
        if requestedbook in self.availablebooks:
            print("The book you requested has now been borrowed")
            self.availablebooks.remove(requestedbook)
        else:
            print("Sorry the book you have requested is currently not in the library")
                  
    def addReturnedBook(self, returnedbook):
        self.availablebooks.append(returnedbook)
        print("Thanks for returning your borrowed book")

    def deleteBook(self, deletebooklibrary):
        if deletebooklibrary in self.availablebooks:
            self.availablebooks.remove(deletebooklibrary)
            print("Book has been deleted from library")
        else:
            print("Book is not avaiable in library to delete")

    def addBook(self, addbooklibrary):
        self.availablebooks.append(addbooklibrary)
        print("Book is successfully Added")

class Librarian:
    def addBookInLibrary(self):
        print("Enter the name of book to be added")
        self.addbook = input()
        return self.addbook

    def deleteBookFromLibrary(self):
        print("Enter the name of book to be deleted")
        self.deletebook = input()
        return self.deletebook

class Student:
    def requestBook(self):
        print("Enter the name of the book you'd like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you'd like to return")
        self.book = input()
        return self.book

if __name__ == "__main__":
    library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
    student=Student()
    librarian = Librarian()
    while True:
       print(""" ======LIBRARY MENU=======
             1. Display all available books
             2. Request a book
             3. Return a book
             4. Add a book in library
             5. Delete a book from library
             6. Exit
             """)
       choice = int(input("Enter Choice:"))
       if choice == 1:
           library.displayAvailableBooks()
       elif choice == 2:
           library.lendBook(student.requestBook())
       elif choice == 3:
           library.addReturnedBook(student.returnBook())
       elif choice == 4:
           library.addBook(librarian.addBookInLibrary())
       elif choice == 5:
           library.deleteBook(librarian.deleteBookFromLibrary())
       elif choice == 6:
           sys.exit()


