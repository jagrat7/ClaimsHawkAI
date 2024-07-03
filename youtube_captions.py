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
# video_id=''

def load_videos():
    try:
        with open('data/videos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"videos": []}

def save_videos(data):
    with open('data/videos.json', 'w') as f:
        json.dump(data, f, indent=2)

def mark_as_processed(data):
    if video['id'] == video_id:
        video['processed'] = True       
    save_videos(data)


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
        if YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US']):
            transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=['en-US'])
        else:
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

def save_full_transcript(video_title, video_date, captions):
    safe_title = sanitize_filename(f"{video_title}_{video_date}")
    filename = f"data/{safe_title}.txt"
    
    full_transcript = " ".join([remove_sound_effects(entry['text']) for entry in captions])
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_transcript)
    
    print(f"Full transcript saved to {filename}")


videos_data = load_videos()

for video in videos_data['videos']:
    video_id = video['id']
    
    # Skip if already processed
    if video.get('processed', False):
        print(f"Skipping already processed video: {video['title']}")
        continue
    
    captions = get_captions(video_id)
    video_title, video_date = get_video_info(video_id)
    
    if captions:
        print(f"Processing Video: {video_title}")
        print(f"Video Date: {video_date}")
        df = save_to_csv(video_id, video_title, video_date, captions)
        save_full_transcript(video_title, video_date, captions)
        print(df.head())  # Display the first few rows of the DataFrame
        
        # Mark as processed
        mark_as_processed(video)
    else:
        print(f"Failed to retrieve captions for video ID: {video_id}")

# Save the updated video data
save_videos(videos_data)




# captions = get_captions(video_id)
# video_title, video_date = get_video_info(video_id)

# if captions:
#     print(f"Video Title: {video_title}")
#     print(f"Video Date: {video_date}")
#     df = save_to_csv(video_id, video_title, video_date, captions)
#     save_full_transcript(video_title, video_date, captions)
#     print(df.head())  # Display the first few rows of the DataFrame
# else:
#     print("Failed to retrieve captions.")
