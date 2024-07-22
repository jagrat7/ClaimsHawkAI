from models.Claim import Claim
from typing import List
from models.Video import Video
from services.langchain_lib import get_claims, load_document, extract_speaker

class ClaimExtractor:
    def __init__(self, input: str) -> None:
        self.input = input

    def extract_claims(self,speaker:str, video: Video) -> List[Claim]:
        # Load the document
        try:
            document = load_document(video.transcript_path)
            
            # Extract speaker
            if not speaker:
                speaker = extract_speaker(video.transcript_path)
            else:
                speaker = speaker
            # Get claims
            claims = get_claims(document[0].page_content, speaker)
            
            return claims
        except Exception as e:
                print(f"Error extracting claims: {str(e)}")
                return []