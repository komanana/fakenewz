import json
from pytube import YouTube
import ssl
import requests
from lxml import etree

ssl._create_default_https_context = ssl._create_unverified_context


def extra_video_data(video_url):
    if 'tiktok' in video_url:
        print(video_url)
        page=requests.get(url='https://www.tiktok.com/oembed?url='+video_url)
        data = json.loads(page.text)
        video_data = {"embed_url": video_url, "video_title": data['title'],"video_id":data['provider_url'],'articleImageLink': data['thumbnail_url'], 'articleUser' : data['author_name']}
        return video_data
        # html = etree.HTML(page)
    else:

        result = YouTube(video_url)
        embed_url = result.embed_url
        video_id=result.video_id
        video_title = result.title
        video_data = {"embed_url": embed_url, "video_title": video_title,"video_id":video_id}
        return video_data
