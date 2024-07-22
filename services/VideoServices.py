import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Video import Video
from services.youtube_captions import get_captions, get_video_info, save_full_transcript

class VideoServices():
    def __init__(self,video:Video) -> None:
        self.video=video

    def get_video_meta(self,video_id:str)->None:
        self.video.title, self.video.date_published = get_video_info(video_id)
        
    def get_captions(self)->str:
        try:
            captions = get_captions()
            if self.video.title  and self.video.date_published:
                self.video.captions_location= save_full_transcript(self.video.title, str(self.video.date_published), captions)
            else:
                print("am i gettting hweurher")
                self.get_video_meta(self.video.id)
                self.video.captions_location= save_full_transcript(self.video.title, str(self.video.date_published), captions)

            self.video.processed = True
            return self.video.captions_location
        except:
            print("Error getting captions")
            return None
