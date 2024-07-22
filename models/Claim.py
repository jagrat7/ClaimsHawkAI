from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base
# class Claim:
#     def __init__(self, speaker:str, claim:str, timestamp:str, measurable:bool, analysis:str,quote:str)->None:
#         self.speaker = speaker
#         self.claim = claim
#         self.measurable = measurable
#         self.analysis = analysis
#         self.timestamp = timestamp
#         self.quote = quote

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    speaker = Column(String)
    claim = Column(String)
    timestamp = Column(String)
    measurable = Column(Boolean)
    analysis = Column(String)
    quote = Column(String)
    video_id = Column(String, ForeignKey("videos.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    video = relationship("Video", back_populates="claims")

    def __str__(self) -> str:
            return f"Claim(speaker={self.speaker}, claim={self.claim}, timestamp={self.timestamp}, measurable={self.measurable}, analysis={self.analysis}, quote={self.quote})"