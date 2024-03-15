from pydantic import BaseModel, AnyUrl
from typing import Dict

class Publication(BaseModel):
    name: str = ""
    publisher: str = ""
    release_date: str = ""
    url: AnyUrl = None
    summary: str = ""
    full_release_date: Dict[str, int] = {}
    website: AnyUrl = None