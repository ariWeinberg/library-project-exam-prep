from fastapi import APIRouter, HTTPException, status, Body
from models.book_view import BookView
from models.book_create import BookCreate
from database.book_db import BookDB


router = APIRouter()


@router.post("/",
              status_code=201,
              response_model=BookView)
def create_book(book: BookCreate = Body()):
    """Handles creation of a new book."""
    book_db=BookDB()
    try:
        new_book_id = book_db.create_book(book)
        new_book = book_db.get_book_by_id(new_book_id)

        if new_book is None:
            raise HTTPException(
                status_code=status.HTTP_500,
                detail=f"failed to create book."
            )

        return new_book
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e)
            )

@router.get("/{book_id}",
              status_code=200,
              response_model=BookView)
def get_book_by_id(book_id: int):
    """Handles creation of a new book."""
    book_db=BookDB()
    try:
        book = book_db.get_book_by_id(book_id)
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No book was found with id: {book_id}.")

        return book
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e)
            )

