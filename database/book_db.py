from email import message

from models import book_create
from models.book_create import BookCreate
from database.db_connection import get_connection
from models.book_view import BookView

STMT_INSERT = """INSERT INTO books 
(`title`, `author`, `genere`, `is_avilable`, `borrowed_by_member_id`)
VALUES
(%s, %s, %s, %s,%s);"""

STMT_SELECT_A_BOOK = """SELECT *
FROM books 
WHERE id = %s
LIMIT 1;"""



class BookDB:
    def create_book(self, new_book: BookCreate):
        conn = get_connection()
        try:
            cur = conn.cursor()
            stmt_parameters = (
                new_book.book_title,
                new_book.book_author,
                new_book.book_genere,
                new_book.book_is_avilable,
                new_book.book_borrowed_by_member_id,
            )
            cur.execute(STMT_INSERT, stmt_parameters)
            new_book_id = cur.lastrowid

            cur.close()
            conn.commit()
            return new_book_id
        finally:
            conn.close()

    def get_book_by_id(self, book_id: int):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            stmt_parameters = (book_id,)
            cur.execute(STMT_SELECT_A_BOOK, stmt_parameters)

            result = cur.fetchone()

            if result is None:
                return None
            
            book: BookView = BookView(**result)

            cur.close()
            conn.commit()
            return book
        finally:
            conn.close()
