import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base
# class Video:
#     def __init__(self, id:str, title:str, processed:bool,captions_location:str)->None:
#         self.id = id
#         self.title = title
#         self.processed = processed
#         self.captions_location = captions_location

class Video(Base):
    __tablename__ = "videos"

    id = Column(String, primary_key=True)
    title = Column(String)
    processed = Column(Boolean, default=False)
    captions_location = Column(String)
    date_published = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    claims = relationship("Claim", back_populates="video")

   
        
