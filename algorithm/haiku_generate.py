import random as rand
from sentences import sentences

num = rand.randint(0,len(sentences)-1)

sentence = ""

for word in sentences[num]:
    sentence += word + " "

print sentence