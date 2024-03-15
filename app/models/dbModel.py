from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")

class DBModelMixin(DateTimeModelMixin):
    id: Optional[str] = Field(None, alias="_id")