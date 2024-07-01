def save_to_csv(video_id, video_title, captions):
    data = []
    window_size = 5  # Number of entries to include in each context window

    for i in range(len(captions)):
        # Get the current entry
        current_entry = captions[i]
        
        # Calculate the start and end of the context window
        start = max(0, i - window_size // 2)
        end = min(len(captions), i + window_size // 2 + 1)
        
        # Create the context by joining the text from the window
        context = " ".join([entry['text'] for entry in captions[start:end]])
        
        # Create a unique ID based on the timestamp of the current entry
        id = f"{video_id}_{int(current_entry['start'] * 1000)}"
        
        # Add the entry to the data
        data.append({
            'id': id,
            'timestamp': current_entry['start'],
            'duration': current_entry['duration'],
            'context': context,
            'current_text': current_entry['text']
        })

    df = pd.DataFrame(data)
    
    # Sanitize the video title for use as a filename
    safe_title = sanitize_filename(video_title)
    filename = f"{safe_title}.csv"
    
    df.to_csv(filename, index=False)
    print(f"Captions saved to {filename}")
    return df
