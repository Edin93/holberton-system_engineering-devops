#!/usr/bin/python3
"""
Module to query the Reddit API and returs the number of subscribers of a
given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a given subreddit.

    Parameters:
    subreddit (string): subreddit to search for.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'my custom user agent 1.0',
    }
    res = requests.get(url, headers=headers)
    try:
        content = res.json()
        return content.get('data', 0).get('subscribers', 0)
    except ImportError:
        return 0
