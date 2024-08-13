#!/usr/bin/python3
"dfdfsdffs"
import requests

def number_of_subscribers(subreddit):
    "sddsfsfsdf"
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (KeyError, ValueError):
            return 0
    else:
        return 0
