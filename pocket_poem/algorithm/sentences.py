# coding=utf-8
import random as rand

from poem.models import Word


# Generate the part of speech desginated by the key
# POS means part of speech
def generatePOS(category, theme=None):
    if theme is not None:
        pos_list = Word.objects.filter(category__name=category, section=theme)
    else:
        pos_list = Word.objects.filter(category__name=category)
    return pos_list[rand.randint(0, len(pos_list) - 1)]


# Generate a random noun
def noun():
    return generatePOS('noun')


# Generate a random verb
def verb():
    return generatePOS('verb')


# Generate a random adverb
def adverb():
    return generatePOS('adverb')


# Generate a random preposition
def preposition():
    return generatePOS('preposition')


# Generate a random adjective
def adjective():
    return generatePOS('adjective')


# Generate a random conjunction
def conjunction():
    return generatePOS('conjunction')


# Generate a random article
def article():
    return generatePOS('article')

# Generate a random pronoun
def pronoun():
    return generatePOS('pronoun')

# List of all the different sentence structures
# Repeated sentence structures are there to increase their likelihood of being chosen
sentence_structures = [
    [article, noun, verb],
    [article, adjective, noun],
    [article, adjective, adjective, noun],
    [article, adjective, noun, verb],
    [article, noun, verb, adverb],
    [pronoun, verb],
    [pronoun, verb, noun],
    [adjective, noun, verb],
    [adjective, noun, verb, adverb],
    [article, noun, verb, article, noun],
    [preposition, article, noun],
    [preposition, article, noun],
    [article, noun, conjunction, article, noun]
]
