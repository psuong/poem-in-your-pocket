# coding=utf-8

import requests
import re
import os
import string

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pocket_poem.settings")

from poem.models import Word

SECTIONS = ['fwd', 'lol', 'win', 'omg', 'cute', 'trashy', 'fail', 'wtf', 'books', 'travel', 'music', 'animals', 'lgbt',
            'sports', 'politics', 'tech', 'entertainment', 'health', 'diy', 'food', 'rewind', 'celebrity', 'comedy',
            'weddings']

BUZZ_FEEDS_ENDPOINT = 'http://www.buzzfeed.com/api/v2/feeds/{0}'
BUZZ_ARTICLES_ENDPOINT = 'http://www.buzzfeed.com/api/v2/buzz/{0}'

CLEAN_REGEX = re.compile('<.*?>')
PUNCTUATIONS = set(string.punctuation)


def clean_html(raw_html):
    return ''.join(ch for ch in re.sub(CLEAN_REGEX, '', raw_html) if ch not in PUNCTUATIONS)


def populate_words(buzz_section=None):
    if buzz_section is None:
        sections = SECTIONS
    else:
        sections = SECTIONS

    for section in sections:
        # Use the section to get all the IDs from BUZZ_FEED_ENDPOINT
        feed_r = requests.get(BUZZ_FEEDS_ENDPOINT.format(section))
        buzzes = feed_r.json()['buzzes']
        for buzz in buzzes:
            # hit all the IDs
            article_r = requests.get(BUZZ_ARTICLES_ENDPOINT.format(buzz['id']))
            sub_buzzes = article_r.json()['buzz']['sub_buzzes']
            for sub_buzz in sub_buzzes:
                for word in clean_html(sub_buzz['description']).split(' '):
                    if not word == word.upper() and word:
                        if not Word.objects.filter(text=word.lower()).exists():
                            # if the found word is not in the database, store it
                            print word

if __name__ == '__main__':
    populate_words()
