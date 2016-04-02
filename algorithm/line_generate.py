import random as rand
from sentences import sentence_structures

def generate_line(syll_count):
    rand_sent_num = rand.randint(0,len(sentence_structures)-1)

    sentence_structure = sentence_structures[rand_sent_num]
    rand_sentence_structure = sentence_structure
    rand_sentence = []
    rand_index = []
    for x in xrange(0,len(rand_sentence_structure)):
        rand_sentence_structure[x] = [rand_sentence_structure[x],x]

    rand.shuffle(rand_sentence_structure)
    for x in xrange(0,len(rand_sentence_structure)):
        rand_index.append(rand_sentence_structure[x][1])
        rand_sentence_structure[x] = rand_sentence_structure[x][0]

    remaining_pos = len(sentence_structure)
    remaining_syll = syll_count
    for generate_word in rand_sentence_structure:
        wordTuple = generate_word()
        word = wordTuple[0]
        word_syll = wordTuple[1]
        if remaining_pos == 1:
            while word_syll != remaining_syll:
                wordTuple = generate_word()
                word = wordTuple[0]
                word_syll = wordTuple[1]        
        else:
            while word_syll > (remaining_syll - remaining_pos + 1):
                wordTuple = generate_word()
                word = wordTuple[0]
                word_syll = wordTuple[1]
        
        remaining_syll -= word_syll
        remaining_pos -= 1
        rand_sentence.append(word)
    sentence = range(len(rand_sentence))
    for x in xrange(0,len(rand_sentence)):
        sentence[rand_index[x]] = rand_sentence[x]

    return " ".join(sentence)