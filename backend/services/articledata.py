from bs4 import BeautifulSoup
import requests
import re
import json

def extract_article_metadata(news_url):

    # dictionary to hold extracted data from article (url, headline, and article image)
    metadata = {"url":news_url, "urlShort": None, "title":None, "image":None, "description":None}

    # User agent to allow access to websites
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # Check validity of URL:
    try:
        response = requests.get(news_url, headers=headers)
    except requests.ConnectionError as connectionException:
        return metadata
    except requests.exceptions.MissingSchema as invalidURLException:
        return metadata

    # Add valid url to return data
    metadata["url"] = news_url

    # Clip to short URL

    # Regex patterns
    first_part_pattern = re.compile(r'http[s]?://')
    second_part_pattern = re.compile(r'/')

    # Start clipping away unnecessary parts of url with regex matches
    clipped_url = news_url

    match = re.search(first_part_pattern, clipped_url)

    idx = match.span()[1]
    clipped_url = clipped_url[idx:]
    
    match = re.search(second_part_pattern, clipped_url)
    idx = match.span()[0]

    clipped_url = clipped_url[:idx]
    metadata["urlShort"] = clipped_url

    # scrape html doc
    source = requests.get(news_url, headers=headers).text
    soup = BeautifulSoup(source, 'lxml')

    # Search meta properties as specified by facebook standards
    title = soup.find("meta", property="og:title")
    img = soup.find("meta", property="og:image")
    desc = soup.find("meta", property="og:description")

    # For twitter url
    if is_twitter_url(news_url):
        title={}
        img={}
        title["content"], img["content"] = get_tweet_info_v2(news_url)


    # Fill dictionary with extracted data
    if title:
        metadata["title"] = title["content"]
    if img:
        metadata["image"] = img["content"]
    if desc:
        metadata["description"] = desc["content"]

    return metadata

def is_twitter_url(url):
    pattern = r'https?://(www\.)?twitter\.com/[^/]+/status/\d+'
    return bool(re.match(pattern, url))

def get_tweet_info_v2(url):
    tweet_id = re.search(r'\d+$', url).group()
    # Needs apply twitter developer bearer_token to use twitter api
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAAA6iQEAAAAA1v057Fix57BOavcs8CUSaL7cr6A%3DX2bWz0ZdqLuz0OBV4bkj7NJLfEeYs2M5im3s9ZVpntVQOrkFly"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    tweet_fields = "tweet.fields=text,attachments"
    media_fields = "media.fields=url"
    expansions = "expansions=attachments.media_keys"
    
    api_url = f"https://api.twitter.com/2/tweets/{tweet_id}?{tweet_fields}&{media_fields}&{expansions}"
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")

    tweet_data = json.loads(response.text)
    title = tweet_data['data']['text']
    image_url = None

    title = re.sub(r'http\S+', '', title).strip()

    if "includes" in tweet_data and "media" in tweet_data["includes"]:
        for media in tweet_data["includes"]["media"]:
            if media["type"] == "photo":
                image_url = media["url"]
                break

    return title, image_url