from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from database.database import get_db
from models.Video import Video
from models.Claim import Claim
from models.schemas import ClaimOutput
from services.ClaimExtractor import ClaimExtractor
from services.VideoServices import VideoServices

router = APIRouter(
    prefix="/claims",
    tags=["claims"],
    responses={404: {"description": "Not found"}}
)

@router.post("/extract/{video_id}")
def extract_claims(video_id: str, db: Session = Depends(get_db)):
    video = db.scalars(select(Video).filter(Video.id == video_id)).first()
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")

    captions_location = VideoServices(video).get_video_captions()
    if not captions_location:
        raise HTTPException(status_code=400, detail="Failed to retrieve captions")
    
    extractor = ClaimExtractor(captions_location)
    claims = extractor.extract_claims(video.speaker, video)    
    
    for claim in claims:  
        print(claim.__str__())
        db_claim = Claim(
            speaker=claim.speaker,
            claim=claim.claim,
            timestamp=claim.timestamp,
            measurable=claim.measurable,  
            analysis=claim.analysis, 
            quote=claim.quote,
            video_id=video_id
        )
        db.add(db_claim)
         
    db.commit() 
    return {"message": f"Extracted and saved {len(claims)} claims for video {video_id}"}

@router.get("/{video_id}", response_model=List[ClaimOutput])
def read_claims(video_id: str, db: Session = Depends(get_db)):
    claims = db.scalars(select(Claim).filter(Claim.video_id == video_id)).all()
    return [ClaimOutput.model_validate(claim.__dict__) for claim in claims]
