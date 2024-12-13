from instagrapi import Client
import os


def search_videos_by_hashtag(username, password, hashtag):
    client = Client()
    try:
        client.login(username, password)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")
        return
    # Initialize the client
   # Replace with your credentials
    
    # Search for posts by hashtag
    medias = client.hashtag_medias_recent(name=hashtag, amount=20)  # Fetch the most recent 20 posts
    
    # Filter only videos
    video_posts = [media for media in medias if media.media_type == 2]  # media_type 2 is for videos
    
    for video in video_posts:
        print(f"Video ID: {video.pk}, URL: {video.video_url}")
    return video_posts


