#!/usr/bin/python3
'Module'

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    "Recursively queries Reddit API for hot article titles and counts keywords"
    if after is None:
        word_count = {w.lower(): 0 for w in word_list}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hds = {
        "User-Agent": "Custum"
    }
    ps = {"after": after, "limit": 100}
    res_ = requests.get(url, headers=hds, params=ps,
                        allow_redirects=False)
    if res_.status_code != 200:
        return
    info_ = res_.json().get("data")
    if not info_:
        return
    child_ = info_.get("children", [])
    for c in child_:
        title = c["data"]["title"]
        for w in title.lower().split():
            if w in word_count:
                word_count[w] += 1
    after = info_.get("after")
    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda item: (-item[1], item[0]))
        for w, C in sorted_word_count:
            if C > 0:
                print(f"{w}: {C}")
