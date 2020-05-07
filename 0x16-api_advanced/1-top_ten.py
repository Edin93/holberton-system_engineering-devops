#!/usr/bin/python3
"""
Module to query the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/new.json'.format(subreddit)
    headers = {
        'User-Agent': 'my custom user agent 1.0',
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    try:
        content = res.json()
        for item in content.get('data').get('children')[0:10]:
            print('{}'.format(item.get('data').get('title')))
    except Exception as e:
        print(None)
