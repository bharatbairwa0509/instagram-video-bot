import os
import requests
from pathlib import Path

def upload_and_post_video_auto(flic_token, title, category_id, public_feed=True):
    try:
        # Step 1: Automatically find the latest video or photo file
        media_dir = Path(r'C:\Users\bhara\OneDrive\Desktop\video-bot')
        media_files = sorted(media_dir.glob('*.*'), key=os.path.getmtime, reverse=True)

        if not media_files:
            print("No media files found in the directory.")
            return

        # Select the most recent file
        video_path = str(media_files[0])
        print(f"Using media file: {video_path}")

        # Step 2: Generate upload URL
        url = "https://api.socialverseapp.com/posts/generate-upload-url"
        headers = {
            "Flic-Token": flic_token,
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Failed to get upload URL:", response.text)
            return

        # Extract upload details
        upload_url = response.json().get("url")
        category = response.json().get("category")
        video_hash = response.json().get("hash")

        if not upload_url or not video_hash:
            print("Invalid response from server while generating upload URL.")
            return

        # Step 3: Upload the video
        with open(video_path, 'rb') as f:
            files = {'file': f}
            upload_response = requests.put(upload_url, data=files)

        if upload_response.status_code == 200:
            print("Video uploaded successfully!")
        else:
            print("Failed to upload video:", upload_response.text)
            return

        # Step 4: Create the post
        url_post = "https://api.socialverseapp.com/posts"
        post_headers = {
            "Flic-Token": flic_token
        }

        # Data for the post request
        post_data = {
            "title": title,
            "hash": video_hash,
            "is_available_in_public_feed": public_feed,
            "category_id": category_id
        }

        post_response = requests.post(url_post, headers=post_headers, json=post_data)

        if post_response.status_code == 200:
            print("Post created successfully!")
            print("Response:", post_response.json())
        else:
            print("Failed to create post!")
            print("Status Code:", post_response.status_code)
            print("Response:", post_response.text)

    except Exception as e:
        print("An error occurred:", str(e))


