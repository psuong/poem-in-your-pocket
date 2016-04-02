from nltk.tag import pos_tag

parts_of_speech = ('article', 'noun', 'verb', 'adjective', 'adverb', 'preposition', 'conjunction')
pos_dict = {'CC': 'conjunction', 'DT': 'article', 'IN': 'proposition', 'JJ': 'adjective', 'JJR': 'adjective',
            'JJS': 'adjective', 'NN': 'noun', 'NNP': 'noun', 'NNPS': 'noun', 'NNS': 'noun', 'PRP': 'noun', 'PRP$': 'noun',
            'RB': 'adverb', 'RBR': 'adverb', 'RBS': 'adverb', 'VB': 'verb', 'VBG': 'verb', 'VBN': 'verb', 'VPN': 'verb',
            'VBZ': 'verb', 'WDT': 'article', 'WP': 'noun', 'WPS': 'noun', 'WRB': 'adverb'}


def pos_thing(word):
    return pos_dict[pos_tag(word)[0][1]]
