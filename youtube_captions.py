from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv
import re, datetime

load_dotenv()

# Set up YouTube API client
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
video_id = 'qqG96G8YdcE'

def get_video_info(video_id):
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

def get_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching captions: {str(e)}")
        return None

def sanitize_filename(filename):
    # Remove invalid characters and replace spaces with underscores
    return re.sub(r'[^\w\-_\. ]', '', filename).replace(' ', '_')

def save_to_csv(video_id, video_title,video_date, captions):
    data = []

    for i in range(len(captions)):
        # Get the current entry
        current_entry = captions[i]
        # Create a unique ID based on the timestamp of the current entry
        id = f"{video_id}_{int(current_entry['start'] )}"
        
        # Add the entry to the data
        data.append({
            'id': id,
            'timestamp': current_entry['start'],
            'duration': current_entry['duration'],
            'context':  current_entry['text'],
        })
    df = pd.DataFrame(data)

    # Sanitize the video title for use as a filename
    safe_title = sanitize_filename(f"{video_title}_{video_date}")
    filename = f"data/{safe_title}.csv"
    
    df.to_csv(filename, index=False)
    print(f"Captions saved to {filename}")
    return df

def save_full_transcript(video_title, video_date, captions):
    safe_title = sanitize_filename(f"{video_title}_{video_date}")
    filename = f"data/{safe_title}.txt"
    
    full_transcript = " ".join([entry['text'] for entry in captions])
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_transcript)
    
    print(f"Full transcript saved to {filename}")


captions = get_captions(video_id)
video_title, video_date = get_video_info(video_id)

if captions:
    print(f"Video Title: {video_title}")
    print(f"Video Date: {video_date}")
    df = save_to_csv(video_id, video_title, video_date, captions)
    save_full_transcript(video_title, video_date, captions)
    print(df.head())  # Display the first few rows of the DataFrame
else:
    print("Failed to retrieve captions.")
