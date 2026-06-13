import os
from dotenv import load_dotenv
from mysql.connector import connect
from mysql.connector.abstracts import MySQLCursorAbstract, MySQLConnectionAbstract


load_dotenv()

STMT_CREATE_TABLE_BOOKS = (
    "CREATE TABLE IF NOT EXISTS books ("
    "`id` INT PRIMARY KEY AUTO_IMCREMENT NOT NULL,"
    "`title` VARCHAR(50) NOT NULL,"
    "`author` VARCHAR(50) NOT NULL,"
    "`genere` ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other'),"
    "`is_avilable` BOOLEAN DEFAULT TRUE NOT NULL,"
    "`borrowed_by_member_id` INT DEFAULT NULL,"
    ");"
)
STMT_CREATE_TABLE_MEMBERS = (
    "CREATE TABLE IF NOT EXISTS members ("
    "`id` INT PRIMARY KEY AUTO_IMCREMENT NOT NULL,"
    "`name` VARCHAR(50) NOT NULL,"
    "`email` VARCHAR(50) UNIQUE NOT NULL,"
    "`is_active` BOOLEAN DEFAULT TRUE NOT NULL,"
    "`total_borrows` INT DEFAULT 0 CHECK(total_borrows >= 0),"
    ");"
)

db_connection_settings = {
    'host': os.environ.get("DB_HOST", "localhost"),
    'port': os.environ.get("DB_PORT", "3306"),
    'user': os.environ.get("DB_USER", "root"),
    'password': os.environ.get("DB_PASSWORD", "root"),
    'database': os.environ.get("DB_NAME", "library_db")
}


def get_connection() -> MySQLConnectionAbstract:
    """Opens and returns a connection to the database."""
    return connect(**db_connection_settings)


def create_tables():
    """Ensures creation of both `books` and `members` tables."""
    conn: MySQLConnectionAbstract = get_connection()
    try:
        cur: MySQLCursorAbstract = conn.cursor()

        _create_table_books(cur=cur)
        _create_table_members(cur=cur)

        cur.close()
        conn.commit()
    finally:
        conn.close()

def _create_table_books(cur: MySQLCursorAbstract):
    """Creates table `books` if not already created."""
    cur.execute(STMT_CREATE_TABLE_BOOKS)

def _create_table_members(cur: MySQLCursorAbstract):
    """Creates table `members` if not already created."""
    cur.execute(STMT_CREATE_TABLE_MEMBERS)



get_connection()

