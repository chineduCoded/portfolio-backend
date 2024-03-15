from pydantic import BaseModel
from typing import List

class Skill(BaseModel):
    name: str = None
    level: str = None
    keywords: List[str] = []
    rating: int = None
    years_of_experience: int = None