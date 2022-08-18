import webbrowser
import feedparser
from random import choice

def main():

    # Get channel url
    channel_url = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCNkIDDoZBwbDG8yQ9IHUN9Q")

    # Grab random video
    video = choice(channel_url.entries)

    # Open video
    webbrowser.open(video.link)

if __name__ == '__main__':
    main()