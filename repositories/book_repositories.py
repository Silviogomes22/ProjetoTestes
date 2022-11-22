from entities.book import Book
from CsvExtract import CsvExtract

class BookRepositories:
    def __init__(self) -> None:
        self.list_books: list[Book] = []

    def set_books(self, file_book : list):
        for book in file_book[1:]:
            list_book = book.split(";")
            book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                        list_book[4], CsvExtract.format_str_price_to_float(list_book[5]))
            self.list_books.append(book)

    def verif_if_book_exists(self, book_id: int) -> bool:
        for book in self.list_books:
            if (book.id == book_id):
                return True
        return False

    def get_book(self,book_id: int):
        for book in self.list_books:
            if (book.id == book_id):
                return book
        return Book(-1, "Book not found!", "", "", "", 0)
