# coding=utf-8
from nltk.tag import pos_tag
from textstat.textstat import textstat

parts_of_speech = ('article', 'noun', 'verb', 'adjective', 'adverb', 'preposition', 'conjunction')
pos_dict = {'CC': 'conjunction', 'DT': 'article', 'IN': 'proposition', 'JJ': 'adjective', 'JJR': 'adjective',
            'JJS': 'adjective', 'NN': 'noun', 'NNP': 'noun', 'NNPS': 'noun', 'NNS': 'noun', 'PRP': 'noun',
            'PRP$': 'noun', 'RB': 'adverb', 'RBR': 'adverb', 'RBS': 'adverb', 'VB': 'verb', 'VBG': 'verb',
            'VBN': 'verb', 'VPN': 'verb', 'VBZ': 'verb', 'WDT': 'article', 'WP': 'noun', 'WPS': 'noun', 'WRB': 'adverb'}


def part_of_speech(word):
    return pos_dict[pos_tag(word)[0][1]]


def syllable_count(word):
    return round(textstat.syllable_count(word))
