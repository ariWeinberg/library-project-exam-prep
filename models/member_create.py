from pydantic import BaseModel, Field


class MemberView(BaseModel):
    """MemberCreate model."""
    member_name: str = Field(max_length=50, alias="name")
    member_email: str = Field(max_length=50, alias="email")
    member_is_active: bool = Field(default=True, alias="is_active")
    member_total_borrows: int = Field(ge=0, default=0, alias="total_borrows")
