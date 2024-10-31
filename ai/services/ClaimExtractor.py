import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.Claim import Claim
from typing import List
from models.Video import Video
from services.langchain_lib import get_claims
class ClaimExtractor:
    def __init__(self, input: str) -> None:
        self.input = input

    def extract_claims(self,speaker:str, video: Video) -> List[Claim]:
        # Load the document
        print("getting to the extract method")
        try:
            # Get claims
            claims = get_claims( speaker,video)
            print("got claims")
            return claims
        except Exception as e:
                print(f"Error extracting claims: {str(e)}")
                return []