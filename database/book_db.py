from models import book_create
from models.book_create import BookCreate
from database.db_connection import get_connection

STMT_INSERT = """INSERT INTO books 
(`title`, `author`, `genere`, `is_avilable`, `borrowed_by_member_id`)
VALUES
(%s, %s, %s, %s,%s);"""



class BookDB:
    def create_book(self, new_book: BookCreate):
        conn = get_connection()
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
        conn.close()
        return new_book_id