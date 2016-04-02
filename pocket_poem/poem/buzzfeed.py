# coding=utf-8

import requests
import re

from poem.models import Word

SECTIONS = ['fwd', 'lol', 'win', 'omg', 'cute', 'trashy', 'fail', 'wtf', 'books', 'travel', 'music', 'animals', 'lgbt',
            'sports', 'politics', 'tech', 'entertainment', 'health', 'diy', 'food', 'rewind', 'celebrity', 'comedy',
            'weddings']

BUZZ_FEEDS_ENDPOINT = 'http://www.buzzfeed.com/api/v2/feeds/{0}'
BUZZ_ARTICLES_ENDPOINT = 'http://www.buzzfeed.com/api/v2/buzz/{0}'

CLEAN_REGEX = re.compile('<.*?>')


def clean_html(raw_html):
    return re.sub(CLEAN_REGEX, '', raw_html)


def populate_words(buzz_section=None):
    if buzz_section is None:
        sections = SECTIONS
    else:
        sections = SECTIONS

    for section in sections:
        # Use the section to get all the IDs from BUZZ_FEED_ENDPOINT
        feed_r = requests.get(BUZZ_FEEDS_ENDPOINT.format(section))
        buzzes = feed_r.json()['buzzes']
        for buzz_id in buzzes['id']:
            # hit all the IDs
            article_r = requests.get(BUZZ_ARTICLES_ENDPOINT.format(buzz_id))
            sub_buzzes = article_r.json()['buzz']['sub_buzzes']
            for sub_buzz in sub_buzzes:
                for word in clean_html(sub_buzz['description']):
                    if not Word.objects.filter(text=word).exists():
                        # if the found word is not in the database, store it
                        pass
