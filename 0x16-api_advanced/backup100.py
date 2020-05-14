#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited
by spaces. Javascript should count as javascript, but java should not).
"""


import json
import re
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
    url = 'https://www.reddit.com/r/{}/.json?after={}'.format(
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
    for article in data.get('children', []):
        for word in word_list:
            pattern = r'(^|\s){}($|\s)'.format(word.lower())
            matches = re.findall(pattern, article.get('data').get('title').lower())
            if len(matches) > 0:
                if word in topics:
                    topics[word] += len(matches)
                else:
                    topics[word] = len(matches)
    if (data.get('after', None) is not None):
        count_words(subreddit, word_list, data.get('after', None))
    else:
        for k in sorted(topics, key=topics.get, reverse=True):
            print(k, ':', topics[k])
