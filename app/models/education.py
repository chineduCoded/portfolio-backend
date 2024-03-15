from pydantic import BaseModel, AnyUrl
from typing import List, Dict

class Education(BaseModel):
    institution: str = ""
    url: AnyUrl = None
    course_studied: str = ""
    study_type: str = ""
    start_date: str = ""
    end_date: str = ""
    score: str = ""
    courses: List[str] = []
    description: str = ""
    activities: str = ""
    start: Dict[str, int] = {}
    end: Dict[str, int] = {}
    website: str = ""
    gpa: str = ""