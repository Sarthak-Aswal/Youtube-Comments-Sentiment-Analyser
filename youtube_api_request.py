from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

def api_request(video_id,max_count):
    load_dotenv()
    api_key = os.getenv("api_key")
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=max_count,)
    response = request.execute()
    return response