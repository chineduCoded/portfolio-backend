from datetime import datetime, timezone

from pydantic import BaseModel

class RWModel(BaseModel):
    class Config:
        """
        Pydantic configuration for the RWModel.
        """
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
        }