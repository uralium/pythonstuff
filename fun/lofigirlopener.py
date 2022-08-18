import webbrowser
import feedparser
from random import choice

def lofi():

    # Get channel url
    channel_url = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCSJ4gkVC6NrvII8umztf0Ow")

    # Grab random video
    video = choice(channel_url.entries)

    # Open video
    print('Playing random song from LofiGirl...')
    webbrowser.open(video.link)

if __name__ == '__main__':
    lofi()