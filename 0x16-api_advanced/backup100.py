#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited
by spaces. Javascript should count as javascript, but java should not).
"""


import json
import requests
import sys

topics = {}
headers = {
    'User-Agent': 'my custom user agent 1.0',
}


def get_url(subreddit, after):
    """
    Return URL of subreddit to request.
    """
    url = 'https://www.reddit.com/r/{}/.json?sort=hot&after={}'.format(
        subreddit, after)
    return url


def count_words(subreddit, word_list, after=None):
    """
    Return a dictionary containing how many times each word
    of the word_list list has been mentioned in the hot articles of
    the given subreddit.
    """
    data = requests.get(get_url(subreddit, after),
                        headers=headers).json().get('data', None)
    if (data is None):
        return None
    for article in data.get('children', None):
        for word in word_list:
            if word.upper() in article.get('data').get('title').upper():
                if word in topics:
                    topics[word] += 1
                else:
                    topics[word] = 1
    if (data.get('after', None) is not None):
        count_words(subreddit, word_list, data.get('after', None))
    else:
        sorted(topics.values())
        for k, v in topics.items():
            print(k, ':', v)
