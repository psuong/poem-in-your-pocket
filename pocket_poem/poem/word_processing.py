# coding=utf-8
from topia.termextract import tag
from textstat.textstat import textstat

parts_of_speech = ('article', 'noun', 'verb', 'adjective', 'adverb', 'preposition', 'conjunction', 'pronoun','proper_noun', 'interjection')
pos_dict = {'CC': 'conjunction', 'DT': 'article', 'IN': 'preposition', 'JJ': 'adjective', 'JJR': 'adjective',
            'JJS': 'adjective', 'NN': 'noun', 'NNP': 'proper_noun', 'NNPS': 'proper_noun', 'NNS': 'noun', 'PRP': 'pronoun',
            'PRP$': 'pronoun', 'RB': 'adverb', 'RBR': 'adverb', 'RBS': 'adverb', 'VB': 'verb', 'VBG': 'verb',
            'VBN': 'verb', 'VPN': 'verb', 'VBZ': 'verb', 'WDT': 'article', 'WP': 'noun', 'WPS': 'noun', 'WRB': 'adverb', 'UH':'interjection'}

tagger = tag.Tagger()
tagger.initialize()


def part_of_speech(word):
    return pos_dict.get(tagger(word)[0][1])


def syllable_count(word):
    return round(textstat.syllable_count(word))
