import feedparser
import requests

import os 
from pathlib import Path
from dotenv import load_dotenv
enviroment_file_path= Path('./env/.env')
load_dotenv(dotenv_path=enviroment_file_path)

ZONEH_RSS_FEED = os.getenv('ZONEH_RSS_FEED_URL')

def get_zoneh():
    url = ZONEH_RSS_FEED
    feed = feedparser.parse(url)
    mongodb_array = []
    for entry in feed.entries:

        mongodb_array.append({
            'title': entry.title,
            'link': entry.link,
            'description': entry.description,
            'published': entry.published,
            'guid': entry.guid
        })
    print(mongodb_array)


def crawl_zoneh():
    get_zoneh()

