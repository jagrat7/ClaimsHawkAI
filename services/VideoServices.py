import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Video import Video
from services.youtube_captions import get_captions, get_video_info, save_full_transcript
from datetime import datetime
class VideoServices():
    def __init__(self,video:Video) -> None:
        self.video=video

    def get_video_meta(self,video_id:str)->None:
        self.video.title, date_str = get_video_info(self.video.id)
        try:
            self.video.date_published = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            self.video.date_published = datetime.strptime(date_str, "%Y-%m-%d")        
    def get_video_captions(self)->str:
        try:
            captions = get_captions(self.video.id)
            if self.video.title  and self.video.date_published:
                self.video.captions_location= save_full_transcript(self.video.title, self.video.date_published, captions)
            else:
                self.get_video_meta(self.video.id)
                self.video.captions_location= save_full_transcript(self.video.title, self.video.date_published, captions)

            self.video.processed = True
            return self.video.captions_location
        except Exception as e:
            print("Error getting captions sdf",e)
            return None

print('hello')