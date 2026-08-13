from pydantic import BaseModel, EmailStr, Field, PastDatetime


class UserCreate(BaseModel):
    username: str = Field(
        ...,
        description="Username of the user",
        max_length=32,
        examples=["john.doe"],
    )
    email: EmailStr = Field(..., description="Email of the user")
    password: str = Field(..., description="Password of the user")
    first_name: str = Field(
        ..., description="First name of the user", max_length=64
    )
    last_name: str = Field(
        ..., description="Last name of the user", max_length=64
    )


class UserResponse(BaseModel):
    id: int = Field(..., description="User ID of the created user")
    username: str = Field(..., description="Username of the user")
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    created_at: PastDatetime
    updated_at: PastDatetime
