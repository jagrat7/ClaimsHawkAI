from database import engine, SessionLocal, Base
from models import Video

from models.Claim import *


Video.__table__.create(bind=engine, checkfirst=True)
Claim.__table__.create(bind=engine, checkfirst=True)

# Sample query to add a video
db = SessionLocal()
try:
    new_video = Video(
        id="assd2343q",
    )
    db.add(new_video)
    db.commit()
    print(f"Added video: {new_video.id}")
finally:
    db.close()