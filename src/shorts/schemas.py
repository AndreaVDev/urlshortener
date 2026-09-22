from datetime import datetime
from pydantic import BaseModel

# API request/response models

# Base model for response to post request
class LinkResponse(BaseModel):
    long_url: str
    short_url: str
    short_code: str
    created_at: datetime
    clicks: int

# Base model for request to post request
class CreateLinkRequest(BaseModel):
    long_url: str