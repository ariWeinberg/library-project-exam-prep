from typing import Literal
from pydantic import BaseModel, Field, model_validator


class MemberView(BaseModel):
    """MemberView model."""
    member_id: int = Field(gt=0, alias="id")
    member_name: str = Field(max_length=50, alias="name")
    member_email: str = Field(max_length=50, alias="email")
    member_is_active: bool = Field(default=True, alias="is_active")
    member_total_borrows: int = Field(ge=0, default=0, alias="total_borrows")
