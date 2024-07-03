from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv
import re, datetime
import json
load_dotenv()

# Set up YouTube API client
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
video_id='nFVUPAEF-sw'


transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US'])
print(transcript)
