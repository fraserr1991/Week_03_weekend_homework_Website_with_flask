from models.book import * 

book_1 = Book("Blockchain Revolution", "Don Tapscott", "Technology", True)
book_2 = Book("Beginners Guide to Google Sheets", "Barrie Roberts", "Computing", False)
book_3 = Book("Mastering Bitcoin", "Andreas M.Antonopoulos", "Technology", False)

books = [book_1, book_2, book_3]

def add_new_book(book):
    books.append(book)

def delete_book_at_index(index):
    books.pop(int(index))

# def show_individual_book(index):