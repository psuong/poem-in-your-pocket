from vocab import vocab
import random as rand

# Generate the part of speech desginated by the key
# POS means part of speech
def generatePOS(key):
	pos_list = vocab[key]
	return pos_list[rand.randint(0,len(pos_list)-1)]

# Generate a random noun
def noun():
	return generatePOS('nouns')
	
# Generate a random verb
def verb():
	return generatePOS('verbs')

# Generate a random adverb
def adverb():
	return generatePOS('adverbs')

# Generate a random preposition
def preposition():
	return generatePOS('prepositions')

# Generate a random adjective
def adjective():
	return generatePOS('adjectives')

# Generate a random conjunction
def conjunction():
	return generatePOS('conjunctions')

# Generate a random article
def article():
	return generatePOS('articles')

# List of all the different sentence structures
# Repeated sentence structures are there to increase their likelihood of being chosen
sentence_structures = [
	[article, noun, verb],
	[article, adjective, noun, verb],
	[article, noun, verb, adverb],
	[adjective, noun, verb],
	[adjective, noun, verb, adverb],
	[article, noun, verb, article, noun],
	[preposition, article, noun],
	[preposition, article, noun],
	[preposition, article, noun],
	[article, noun, conjunction, article, noun]
]