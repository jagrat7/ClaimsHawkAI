from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from database.database import get_db
from models.Video import Video
from models.schemas import VideoInput, VideoOutput
from services.VideoServices import VideoServices

router = APIRouter(
    prefix="/videos",
    tags=["videos"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=VideoOutput)
def create_video(video: VideoInput, db: Session = Depends(get_db)):
    db_video = Video(id=video.id, speaker=video.speaker, processed=False)
    VideoServices(db_video).get_video_meta(db_video.id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

@router.get("/{video_id}", response_model=VideoOutput)
def get_video(video_id: str, db: Session = Depends(get_db)):
    db_video = db.scalars(select(Video).filter(Video.id == video_id)).first()
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")       
    return db_video

@router.get("/", response_model=List[VideoOutput])
def get_all_videos(db: Session = Depends(get_db)):
    db_videos = db.scalars(select(Video)).all()
    return [VideoOutput.model_validate(video) for video in db_videos]
