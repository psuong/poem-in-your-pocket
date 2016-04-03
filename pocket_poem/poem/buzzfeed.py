# coding=utf-8
import requests
import re
import os
import string

from poem.models import Word, Category
from poem.word_processing import syllable_count, part_of_speech
from poem.categories import PARTS_OF_SPEECH

SECTIONS = ['fwd', 'lol', 'win', 'omg', 'cute', 'trashy', 'fail', 'wtf', 'books', 'travel', 'music', 'animals', 'lgbt',
            'sports', 'politics', 'tech', 'entertainment', 'health', 'diy', 'food', 'rewind', 'celebrity', 'comedy',
            'weddings']

BUZZ_FEEDS_ENDPOINT = 'http://www.buzzfeed.com/api/v2/feeds/{0}'
BUZZ_ARTICLES_ENDPOINT = 'http://www.buzzfeed.com/api/v2/buzz/{0}'

CLEAN_REGEX = re.compile('<.*?>')
PUNCTUATIONS = set(string.punctuation)


def clean_html(raw_html):
    return ''.join(ch for ch in re.sub(CLEAN_REGEX, '', raw_html) if ch not in PUNCTUATIONS or ch == '\'')


def clean_punctuation(sentence):
    return ''.join(ch for ch in sentence if ch not in PUNCTUATIONS or ch == '\'')


def populate_categories():
    for category in PARTS_OF_SPEECH:
        Category.objects.get_or_create(name=category[0])


def populate_words(buzz_section=None):
    if buzz_section is None:
        sections = SECTIONS
    else:
        sections = buzz_section

    for section in sections:
        print section
        # Use the section to get all the IDs from BUZZ_FEED_ENDPOINT
        feed_r = requests.get(BUZZ_FEEDS_ENDPOINT.format(section))
        buzzes = feed_r.json()['buzzes']
        for buzz in buzzes:
            # hit all the IDs
            article_r = requests.get(BUZZ_ARTICLES_ENDPOINT.format(buzz['id']))
            buzz_title = article_r.json()['buzz']['title']
            for word in clean_punctuation(buzz_title).split(' '):
                if not word == word.upper() and word:
                    # store the word
                    category = part_of_speech(word.lower())
                    if category is not None:
                        if not Word.objects.filter(text=word.lower(), section=section).exists():
                            Word.objects.get_or_create(text=word.lower(),
                                                       syllable_count=syllable_count(word.lower()),
                                                       article_id=buzz['id'],
                                                       category=Category.objects.get(name=category),
                                                       section=section)
