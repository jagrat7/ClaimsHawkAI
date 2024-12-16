from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv
import re
from datetime import datetime
import json
load_dotenv()

# Set up YouTube API client
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

# Change the file_location to use absolute path
file_location = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/')
# video_id=''


def get_video_info(video_id):
    print(f"Getting video info for video ID in youtubee: {video_id}")
    try:
        response = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=video_id
        ).execute()
        if 'items' in response and len(response['items']) > 0:
            snippet = response['items'][0]['snippet']
            title = snippet['title']
            published_at = snippet['publishedAt']
            # Convert the published_at string to a datetime object
            # date = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
            return title, published_at
        else:
            return "Title not found", "Date not found"
    except Exception as e:
        print(f"Error fetching video info: {str(e)}")
        return "Error fetching title", "Error fetching date"

def save_full_transcript(video_title, video_date, captions):
    try:
        # Create the data directory if it doesn't exist
        os.makedirs(file_location, exist_ok=True)
        
        safe_title = sanitize_filename(f"{video_title}_{video_date}")
        print("Creating the transcript file.....")
        filename = os.path.join(file_location, f"{safe_title}.txt")
        print("filename:", filename)
        
        full_transcript = " ".join([remove_sound_effects(entry['text']) for entry in captions])
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_transcript)
        print(f"Successfully saved transcript to {filename}")
        return filename
    except Exception as e:
        print(f"Error saving full transcript: {str(e)}")
        return None

def get_captions(video_id):
    try:
        # if YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US']):
        #     transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=['en-US'])
        # else:
        print("am i gettting in the youtube ")

        transcript = YouTubeTranscriptApi.get_transcript(video_id,preserve_formatting=True)
        return transcript
    except Exception as e:
        print(f"Error fetching captions: {str(e)}")
        return None

def sanitize_filename(filename):
    # Remove invalid characters and replace spaces with underscores
    return re.sub(r'[^\w\-_\. ]', '', filename).replace(' ', '_')
def remove_sound_effects(text):
    # Remove text within parentheses or square brackets
    return re.sub(r'\([^)]*\)|\[[^]]*\]', '', text).strip()
def save_to_csv(video_id, video_title, video_date, captions):
    data = []
    
    for entry in captions:
        timestamp = entry['start']
        text = remove_sound_effects(entry['text'])
        
        data.append({
            'timestamp': timestamp,
            'text': text.strip()
        })

    df = pd.DataFrame(data)

    # Sanitize the video title for use as a filename
    safe_title = sanitize_filename(f"{video_title}_{video_date}")
    filename = file_location+ f"{safe_title}.csv"
    
    df.to_csv(filename, index=False)
    print(f"Captions saved to {filename}")
    return df

def save_to_csv2(video_id, video_title, video_date, captions):
    data = []
    current_minute = 0
    current_text = ""
    min_words = 1  # Minimum number of words for a row to be included

    for entry in captions:
        start_time = entry['start']
        text = remove_sound_effects(entry['text'])
        
        if start_time // 60 > current_minute:
            if current_text and len(current_text.split()) >= min_words:
                data.append({
                    'id': f"{video_id}_{current_minute}",
                    # 'timestamp': current_minute * 60,
                    'context': current_text.strip()
                })
            current_minute = start_time // 60
            current_text = text
        else:
            current_text += " " + text
    
    # Add the last minute if there's any remaining text
    if current_text and len(current_text.split()) >= min_words:
        data.append({
            'id': f"{video_id}_{current_minute}",
            # 'timestamp': current_minute * 60,
            'context': current_text.strip()
        })

    df = pd.DataFrame(data)

    # Sanitize the video title for use as a filename
    safe_title = sanitize_filename(f"{video_title}_{video_date}")
    filename = f"data/{safe_title}.csv"
    
    df.to_csv(filename, index=False)
    print(f"Captions saved to {filename}")
    return df


print('hello')