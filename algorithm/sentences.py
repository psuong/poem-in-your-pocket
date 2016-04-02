from vocab import vocab
import random as rand

def noun():
	nounList = vocab['nouns']
	return nounList[rand.randint(0,len(nounList)-1)][0]
	
def verb():
	verbList = vocab['verbs']
	return verbList[rand.randint(0,len(verbList)-1)][0]

sentences = [
	(noun(), verb()),
	(noun(), verb(), noun())
]