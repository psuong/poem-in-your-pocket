from vocab import vocab
import random as rand

# POS means part of speech
def generatePOS(key):
	pos_list = vocab[key]
	return pos_list[rand.randint(0,len(pos_list)-1)]

def noun():
	return generatePOS('nouns')
	
def verb():
	return generatePOS('verbs')

def adverb():
	return generatePOS('adverbs')

def preposition():
	return generatePOS('prepositions')

def adjective():
	return generatePOS('adjectives')

def conjunction():
	return generatePOS('conjunctions')

def article():
	return generatePOS('articles')

sentence_structures = [
	[article, noun, verb],
	[article, noun, verb, adverb],
	[noun, verb],
	[noun, verb, adverb],
	[noun, verb, noun]
]