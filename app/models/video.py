from pydantic import BaseModel, AnyUrl
from typing import List

class Video(BaseModel):
    url: AnyUrl = None
    source: str = None
    source_id: str = None