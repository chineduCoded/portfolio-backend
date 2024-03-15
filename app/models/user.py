from datetime import datetime
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    HttpUrl,
     validator,
     ConfigDict,
)
from .rwmodel import RWModel
from .dbModel import DBModelMixin
from .custom_types import PydanticObjectId





class OauthException(BaseModel):
    detail: str


class UnauthorizedException(BaseModel):
    detail: str


class OauthToken(BaseModel):
    access_token: str
    token_type: str

class OauthTokenData(BaseModel):
    username: str | None = None


class UserInCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserInResponse(BaseModel):
    message: str
    id: PydanticObjectId | None = Field(None, alias="_id")

    model_config = ConfigDict(
        populate_by_name=True,
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        validate_assignment=True
    )

class User(BaseModel):
    id: PydanticObjectId = Field(..., alias="_id")
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(
        populate_by_name=True,
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        validate_assignment=True
    )