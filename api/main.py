from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select,inspect
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import SessionLocal, create_tables,engine
from models.Video import Video
from models.Claim import Claim
from pydantic import BaseModel
from typing import List
from datetime import datetime
from services.ClaimExtractor import ClaimExtractor
from services.VideoServices import VideoServices
from typing import Optional 
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try: 
        inspector = inspect(engine)
        if not inspector.has_table("videos") or not inspector.has_table("claims"):
            create_tables()
            print("Tables created successfully")
        yield db
    finally:
        db.close()


class VideoInput(BaseModel):
    id: str
    speaker:str

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

@app.post("/videos/", response_model=VideoInput) 
def create_video(video: VideoInput, db: Session = Depends(get_db)):
    db_video = Video(id=video.id, speaker= video.speaker, processed=False)
    VideoServices(db_video).get_video_meta(db_video.id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

@app.get("/videos/{video_id}", response_model=VideoOutput)
def get_video(video_id: str, db: Session = Depends(get_db)):
    db_video = db.scalars(select(Video).filter(Video.id == video_id)).first()
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")       
    return db_video 
 
@app.get("/videos/", response_model=List[VideoOutput])
def get_all_videos(db: Session = Depends(get_db)): 
    db_videos = db.scalars(select(Video)).all()
    return [VideoOutput.model_validate(video) for video in db_videos]

@app.post("/extract_claims/{video_id}")
def extract_claims(video_id: str, db: Session = Depends(get_db)):
    video = db.scalars(select(Video).filter(Video.id == video_id)).first()
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")

    captions_location = VideoServices(video).get_video_captions()
    if not captions_location:
        raise HTTPException(status_code=400, detail="Failed to retrieve captions")
    
    extractor = ClaimExtractor(captions_location)
    claims = extractor.extract_claims(video.speaker, video)    
    counter=0 
    for claim in claims:  
        print(claim.__str__())
        db_claim = Claim(speaker=claim.speaker,
            claim=claim.claim,
            timestamp=claim.timestamp,
            measurable=claim.measurable,  
            analysis=claim.analysis, 
            quote=claim.quote,video_id=video_id)
        db.add(db_claim)
         
    db.commit() 
    return {"message": f"Extracted and saved {len(claims)} claims for video {video_id}"}

@app.get("/claims/{video_id}", response_model=List[ClaimOutput])
def read_claims(video_id: str, db: Session = Depends(get_db)):
    claims = db.scalars(select(Claim).filter(Claim.video_id == video_id)).all()
    return [ClaimOutput.model_validate(claim.__dict__) for claim in claims]
