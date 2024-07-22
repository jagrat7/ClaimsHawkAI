from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import SessionLocal, engine
from models.Video import Video
from models.Claim import Claim
from pydantic import BaseModel
from typing import List
from datetime import datetime
from services.ClaimExtractor import ClaimExtractor
from services.VideoServices import VideoServices
from typing import Optional


app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class VideoInput(BaseModel):
    id: str

class ClaimInput(BaseModel):
    content: str
    video_id: str
class VideoOutput(BaseModel):
    id: str
    title: Optional[str] = None
    processed: bool
    captions_location: Optional[str] = None
    date_published: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


@app.post("/videos/", response_model=VideoInput)
def create_video(video: VideoInput, db: Session = Depends(get_db)):
    db_video = Video(id=video.id, processed=False)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

@app.get("/videos/{video_id}", response_model=VideoInput)
def get_video(video_id: str, db: Session = Depends(get_db)):
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@app.get("/videos/", response_model=List[VideoOutput])
def get_all_videos(db: Session = Depends(get_db)):
    db_videos = db.query(Video).all()
    return [VideoOutput.from_orm(video) for video in db_videos]

@app.post("/extract_claims/{video_id}")
def extract_claims(video_id: str, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    print("what am i getting",video.id)
    video_service = VideoServices(video)
    captions_location = video_service.get_captions()
    print("cap loction debug",video.title)
    if not captions_location:
        raise HTTPException(status_code=400, detail="Failed to retrieve captions")
    
    extractor = ClaimExtractor(captions_location)
    claims = extractor.extract_claims("", video)
    
    for claim in claims:
        db_claim = Claim(**claim.dict(), video_id=video_id)
        db.add(db_claim)
    
    db.commit()
    return {"message": f"Extracted and saved {len(claims)} claims for video {video_id}"}


@app.get("/claims/{video_id}", response_model=List[ClaimInput])
def read_claims(video_id: str, db: Session = Depends(get_db)):
    claims = db.query(Claim).filter(Claim.video_id == video_id).all()
    return claims

