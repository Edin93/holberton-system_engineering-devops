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
    subreddit_subscribers = 0
    url = 'https://www.reddit.com/subreddits/search.json?q={}'.format(
        subreddit)
    headers = {
        'User-Agent': 'my custom user agent 1.0',
    }
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        content = res.json()
        children = content.get('data', 0).get('children', 0)
        if children:
            subreddit_subscribers = children[0].get('data', 0).get(
                'subscribers', 0)
        return subreddit_subscribers
    except requests.exceptions.AttributeError as e:
        return 0
