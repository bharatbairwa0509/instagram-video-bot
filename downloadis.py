from dotenv import load_dotenv
import os
import requests
import tqdm
# Load variables from the .env file
load_dotenv()

from instagrapi import Client


def download_media_with_progress(username, password, post_url):
    # Initialize the client
    client = Client()
    try:
        client.login(username, password)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    try:
        # Get media ID from the URL (whether it's a post, video, or reel)
        media_id = client.media_pk_from_url(post_url)

        # Get media info (this will work for posts, reels, and videos)
        media_info = client.media_info(media_id)
        
        # Check if the media is a video or image
        if media_info.media_type == 2:  # 2 is for video
            media_url = media_info.video_url  # Video URL for reels/posts with videos
            file_extension = ".mp4"
        else:
            media_url = media_info.thumbnail_url  # Image URL for posts with images
            file_extension = ".jpg"  # Save as JPG if it's an image

        if not media_url:
            print("No media found at the provided URL.")
            return

        # Get file size for progress bar
        response = requests.head(media_url)
        total_size = int(response.headers.get('content-length', 0))


        videos_dir = "videos"
        os.makedirs(videos_dir, exist_ok=True)

        # Use the media ID as the file name and save it in the videos directory
        file_name = os.path.join(videos_dir, f"media_{media_id}{file_extension}")

        

        # Stream download with progress bar
        with requests.get(media_url, stream=True) as r, open(file_name, "wb") as f, tqdm.tqdm(
            desc=f"Downloading",
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            # Iterate over the chunks and write to file
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))  # Update progress bar

        print(f"Media downloaded {file_name}")
    
    except Exception as e:
        print(f"Error: {e}")




