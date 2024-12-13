from downloadis   import download_media_with_progress
from uploadsocial   import upload_and_post_video_auto
from search_hastage   import  search_videos_by_hashtag
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    while True:




        print("\nChoose an option:")
        print("1. Search videos by hashtag")
        print("2. Download a video")
        print("3. Upload and post a video")
        print("4. Exit")

        choice = input("Enter your choice: ")
        instagram_USERNAME= input(" Enter YOur Username=")
        instagram_password = input("Enter your password = ")

        if choice == "1":
            hashtag = input("Enter the hashtag to search for: ")
            videos = search_videos_by_hashtag(instagram_USERNAME, instagram_password, hashtag)
            if videos:
                print(f"Found {len(videos)} videos.")
            else:
                print("No videos found.")

        elif choice == "2":
            video_url = input("Enter the video URL to download: ")
            download_media_with_progress(instagram_USERNAME , instagram_password ,video_url)

        elif choice == "3":
            video_path = input("Enter the path to the video file: ")
            title = input("Enter the title for the post: ")
            category_id = int(input("Enter the category ID: "))
            flic_token = os.getenv("flic_token")
            upload_and_post_video_auto(flic_token, video_path, title, category_id)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
