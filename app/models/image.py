from pydantic import BaseModel, AnyUrl
from typing import List

class ImageResolution(BaseModel):
    url: AnyUrl = ""
    size: int = None
    width: int = None
    height: int = None

class ImageResolutions(BaseModel):
    micro: ImageResolution
    thumbnail: ImageResolution
    mobile: ImageResolution
    desktop: ImageResolution

class Image(BaseModel):
    resolutions: ImageResolutions
