# ISBN contains simple digits without dashes
class Book:
    def __init__(self, isbn_nr, title_tx, author_tx, year_int):
        self.isbn = isbn_nr
        self.title = title_tx
        self.author = author_tx
        self.year = year_int

# state could be: in_library and borrowed.  Depending of the location
class BookCopy:
    def __init__(self, original_book):
        self.state = 'in_library'
        self.book = original_book

# Distributor has new publicised books available for library
class Distributor:
    def __init__(self):
        self.books = []

    def create_book(self, isbn_nr, title_tx, author_tx, year_int):
        new_book = Book(isbn_nr, title_tx, author_tx, year_int)
        if self.check_for_dublicate(new_book.isbn):
            print("The same ISBN number is in the list!")
        else:
            self.books.append(new_book)

    def list_books(self):
        # isbn_arr = map()
        list_books_in_console(self.books)

    def check_for_dublicate(self, isbn_nr):
        # get all isbn numbers in list
        isbn_list = []
        for book in self.books:
            isbn_list.append(book.isbn)
        # check list for the same isbn
        if isbn_nr in isbn_list:
            return True
        else:
            return False

    def get_book(self, nr):
        return self.books[nr - 1]


# Create library class

class Library:
    def __init__(self):
        self.books = []

    def buy_book(self, book_nr):
        original_book = distributor.get_book(book_nr)
        book_copy = BookCopy(original_book)
        self.books.append(book_copy)
        print(f'Bought book {book_copy}')

    def list_books(self):
        list_books_in_console(self.books, True)

    # borrow_book()
    # return_book()
    # search_book(author, title)


# app loop
if __name__ == '__main__':
    distributor = Distributor()
    library = Library()

    # load default books
    distributor.create_book(100, 'title1', 'author1', 2001)
    distributor.create_book(101, 'title2', 'author2', 2002)
    distributor.create_book(101, 'title3', 'author3', 2003)
    distributor.create_book(103, 'title4', 'author4', 2004)


    # console functions

    def get_new_book_inputs():
        print('*all inputs are required!')
        isbn_nr = input("Enter book's ISBN number (only numbers): ")
        title_tx = input("Enter book's title: ")
        author_tx = input("Enter book's author: ")
        year_nr = input("Enter year of publication (only numbers): ")
        return isbn_nr, title_tx, author_tx, year_nr



    def list_books_in_console(book_arr, copy=False):
        if len(book_arr) > 0:
            print('------ LIST OF AVAILABLE BOOKS ------')
            nr = 1
            if not copy:
                for book in book_arr:
                    print(f'{nr}. {book.isbn} {book.title} {book.author} {book.year}')
                    nr += 1

            else:
                for book in book_arr:
                    print(f'{nr}. {book.book.isbn} {book.book.title} {book.book.author} {book.book.year}')
                    nr += 1
        else:
            print('There no books to list.')


    # for x in test_list:
    #     if x.value == value:
    #         print("i found it!")
    #         break

    isQuit = False
    while not isQuit:
        print('''
        ------ LIBRARY MENU ------
        
        1. Create new book (publish)
        2. List of published books
        3. Buy book
        4. List books of library
        5. Borrow book
        6. Return book
        7. Search book
        8. Quit
        ''')
        try:
            menu_nr = int(input('Enter menu number (1-8): '))
        except ValueError:
            print('Choose from 1 to 8!')
        else:
            match menu_nr:
                case 1:
                    isbn, title, author, year = get_new_book_inputs()
                    distributor.create_book(isbn, title, author, year)
                case 2:
                    distributor.list_books()
                case 3:
                    distributor.list_books()
                    book_nr = int(input('Enter row number of book to buy: (exm. 1 to buy first book) :'))
                    library.buy_book(book_nr)

                case 4:
                    library.list_books()
                case 5:
                    print('5')
                case 6:
                    print('6')
                case 7:
                    print('7')
                case 8:
                    isQuit = True
                case _:
                    print('Choose from 1 to 8!')
