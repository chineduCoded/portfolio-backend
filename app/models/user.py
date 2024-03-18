import string
from datetime import datetime
from typing import Optional, Annotated
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    AnyHttpUrl,
     validator,
     ConfigDict,
)
from .custom_types import PydanticObjectId


class OauthException(BaseModel):
    detail: str


class UnauthorizedException(BaseModel):
    detail: str


class OauthToken(BaseModel):
    access_token: str
    token_type: str

class OauthTokenData(BaseModel):
    user_id: Optional[PydanticObjectId] = Field(None, alias="_id")
    username: Optional[str] = None

    model_config = ConfigDict(
        populate_by_name=True,
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        validate_assignment=True
    )

class UserBase(BaseModel):
    username: str
    email: EmailStr
    image_url: Optional[str] = ""
    github_url: Optional[str] = ""
    blog_url: Optional[str] = ""
    bio: Optional[str] = ""
    disabled: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserInCreate(BaseModel):
    username: Annotated[str, Field(..., min_length=5, max_length=25, pattern="^[a-zA-Z0-9_-]+$", to_lower=True)]
    email: EmailStr
    password: Annotated[str, Field(..., min_length=8, max_length=16)]


class UserInDB(UserBase):
    password: str

class UserCreateResponse(BaseModel):
    message: str
    id: PydanticObjectId = Field(..., alias="_id")

    model_config = ConfigDict(
        populate_by_name=True,
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        validate_assignment=True
    )

class User(UserBase):
    id: PydanticObjectId = Field(..., alias="_id")
    model_config = ConfigDict(
        populate_by_name=True,
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        validate_assignment=True
    )

class CountUser(BaseModel):
    total_users: int

class UserInUpdate(BaseModel):
    username: Optional[Annotated[str, Field(None, min_length=5, max_length=25, pattern="^[a-zA-Z0-9_-]+$")]] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    image_url: Optional[str] = ""
    github_url: Optional[str] = ""
    blog_url: Optional[str] = ""
    bio: Optional[str] = ""
    disabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None