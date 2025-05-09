import requests
import pandas as pd
import time
from datetime import datetime
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file (optional)
load_dotenv()

# API key
API_KEY = os.getenv('API_KEY')

#Environment variableS
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

#  Configuration
CHANNEL_ID = 'UC7cs8q-gJRlGwj4A8OmCmXg'
OUTPUT_FILENAME = os.getenv('OUTPUT_FILENAME')

# YouTube Data API v3 key
API_KEY = os.getenv('API_KEY')
CHANNEL_USERNAME = 'AlexTheAnalyst'

# Initialize API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

channel_id = 'UC7cs8q-gJRlGwj4A8OmCmXg'
#	res = youtube.channels().list(forUsername=username, part='id').execute()
#	return res['items'][0]['id']

def get_uploads_playlist_id(channel_id):
    res = youtube.channels().list(part='contentDetails', id=channel_id).execute()
    return res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_all_video_ids(playlist_id):
    video_ids = []
    next_page_token = None

    while True:
        res = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        video_ids += [item['contentDetails']['videoId'] for item in res['items']]
        next_page_token = res.get('nextPageToken')

        if not next_page_token:
            break

    return video_ids

def get_video_details(video_ids):
    all_data = []

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        res = youtube.videos().list(part='snippet,statistics', id=','.join(batch)).execute()

        for video in res['items']:
            snippet = video['snippet']
            stats = video['statistics']

            all_data.append({
                'video_id': video['id'],
                'title': snippet['title'],
                'publish_time': snippet['publishedAt'],
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0))
            })

    return pd.DataFrame(all_data)

if __name__ == '__main__':
    print('Fetching channel ID...')
    
    print('Getting uploads playlist ID...')
    playlist_id = get_uploads_playlist_id(channel_id)

    print('Getting all video IDs...')
    video_ids = get_all_video_ids(playlist_id)

    print(f'Total videos found: {len(video_ids)}')

    print('Fetching video details...')
    df = get_video_details(video_ids)

    df['publish_time'] = pd.to_datetime(df['publish_time'])
    df['like_to_view_ratio'] = df['likes'] / df['views']

    print(df.head())
    df.to_csv('alex_videos.csv', index=False)
    print('Data saved to alex_videos.csv ✅')
