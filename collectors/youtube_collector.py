from googleapiclient.discovery import build
from datetime import datetime, timedelta
from core.config import YOUTUBE_API_KEY, FETCH_INTERVAL_MINUTES
import json

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def fetch_youtube_posts(config):

    keywords = config["keywords"] if isinstance(config["keywords"], list) else json.loads(config["keywords"])

    # Combine keywords into one query
    query = " OR ".join(keywords[:10])

    # Calculate last FETCH_INTERVAL_MINUTES window
    published_after = (datetime.utcnow() - timedelta(minutes=FETCH_INTERVAL_MINUTES)).isoformat("T") + "Z"

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=50,
        regionCode="IN",
        order="date",
        publishedAfter=published_after   # IMPORTANT FILTER
    )

    response = request.execute()

    videos = []

    for item in response.get("items", []):

        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        video_id = item["id"]["videoId"]

        video = {
            "id": video_id,
            "text": title + " " + description,
            "channel": item["snippet"]["channelTitle"],
            "url": f"https://youtube.com/watch?v={video_id}",
            "published_at": item["snippet"]["publishedAt"]
        }

        videos.append(video)

    return videos