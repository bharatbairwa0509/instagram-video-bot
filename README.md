# Instagram Video Bot

## Overview
This project is a Python-based bot that interacts with Instagram to search for videos by hashtags, download them, and upload them to a custom server using provided APIs. The bot provides a command-line interface to manage these operations seamlessly.

## Features
- **Search Videos by Hashtag**: Fetch the most recent video posts for a specific hashtag from Instagram.
- **Download Videos**: Download videos with a progress bar and save them locally.
- **Upload Videos**: Upload videos to a custom server and create a post with a title and category.

## Prerequisites
- Python 3.7+
- Instagram account credentials.
- Flic-Token for server authentication.
- Required Python libraries (see Installation section).

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create a `.env` file in the project root and add the following variables:
    ```env
    USER_NAME=<your_instagram_username>
    PASSWORD=<your_instagram_password>
    FLIC_TOKEN=<your_flic_token>
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage

When you run the bot, you will be presented with the following options:

1. **Search videos by hashtag**:
   - Enter a hashtag to fetch recent video posts.

2. **Download a video**:
   - Provide the URL of a video to download it locally.

3. **Upload and post a video**:
   - Provide the path to the video file, a title, and a category ID to upload and create a post on the server.

4. **Exit**:
   - Exit the program.

## File Structure
```
project-folder/
├── main.py           # Main program file with user interaction
├── requirements.txt  # Python dependencies
├── .env              # Environment variables
├── README.md         # Project documentation
```

## Dependencies
- `instagrapi`: For interacting with Instagram.
- `requests`: For handling HTTP requests.
- `tqdm`: For displaying progress bars during downloads.
- `python-dotenv`: For managing environment variables.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Notes
- Ensure your Instagram credentials are correct in the `.env` file.
- The `FLIC_TOKEN` is required for uploading videos to the custom server.
- Use valid category IDs when creating posts.


## Author
Developed by bharat bairwa.

