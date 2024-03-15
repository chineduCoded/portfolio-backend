from pydantic import BaseModel
from typing import Dict

class Award(BaseModel):
    title: str = ""
    date: str = ""
    awarder: str = ""
    summary: str = ""
    full_date: Dict[str, int] = {}       