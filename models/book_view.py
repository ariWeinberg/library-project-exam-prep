from turtle import mode

from pydantic import BaseModel, Field, model_validator
from typing import Literal


class BookCreate(BaseModel):
    book_id: int = Field(gt=0, alias="id")
    book_title: str = Field(max_length=50, alias="title")
    book_author: str = Field(max_length=50, alias="author")
    book_genere: Literal['Fiction', 'Non-Fiction', 'Science', 'History', 'Other'] = Field(alias="genere")
    book_is_avilable: bool = Field(default=True, alias="is_avilable")
    book_borrowed_by_member_id: int | None = Field(gt=0, default=None, alias="borrowed_by_member_id")

    @model_validator(mode='after')
    def validate_avilability(self):
        """Validate that avilability and borrowing rules are kept."""
        if (self.book_is_avilable == True) and (self.book_borrowed_by_member_id is not None):
            message = f"borrowed_by_member_id can not be set when is_avilable is True."
            raise ValueError (message)

        if (self.book_is_avilable == False) and (self.book_borrowed_by_member_id is None):
            message = f"borrowed_by_member_id must be set when is_avilable is not."
            raise ValueError (message)

