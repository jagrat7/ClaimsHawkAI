from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VideoInput(BaseModel):
    id: str
    speaker: str

class VideoOutput(BaseModel):
    id: str
    speaker: Optional[str] = None
    title: Optional[str] = None
    processed: bool
    captions_location: Optional[str] = None
    date_published: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
 
    class Config:
        from_attributes = True 

class ClaimOutput(BaseModel):
    id: int
    speaker: str
    claim: Optional[str] = None
    timestamp: str
    measurable: bool
    analysis: str
    quote: str
    video_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
