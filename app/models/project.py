from pydantic import BaseModel, AnyUrl
from typing import List, Dict
from . image import Image
from . video import Video

class Project(BaseModel):
    name: str = ""
    description: str = ""
    url: AnyUrl = None
    highlights: List[str] = []
    keywords: List[str] = []
    roles: List[str] = []
    start_date: str = ""
    end_date: str = ""
    entity: str = ""
    project_type: str = ""
    display_name: str = ""
    website: AnyUrl = None
    summary: str = ""
    primary_language: str = ""
    languages: List[str] = []
    libraries: List[str] = []
    frameworks: List[str] = []
    tools: List[str] = []
    github_url: AnyUrl = None
    repository_url: AnyUrl = None
    start: Dict[str, int] = {}
    end: Dict[str, int] = {}
    images: List[Image] = []
    videos: List[Video] = []