from pydantic import BaseModel, AnyUrl
from typing import List, Dict

class Experience(BaseModel):
    name: str = ""
    location: str = ""
    description: str = ""
    position: str = ""
    url: AnyUrl = None
    start_date: str = ""
    end_date: str = ""
    summary: str = ""
    highlights: List[str] = []
    is_current_role: bool = False
    start: Dict[str, int] = {}
    end: Dict[str, int] = {}
    company: str = ""
    website: AnyUrl = None