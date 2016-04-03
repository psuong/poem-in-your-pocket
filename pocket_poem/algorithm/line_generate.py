import random as rand
from copy import deepcopy
from sentences import sentence_structures


def generate_line(syll_count, theme=None):
    """
    Generates a random line of haiku with the given syll_count
    """
    rand_sent_num = rand.randint(0, len(sentence_structures) - 1)
    sentence_structure = sentence_structures[rand_sent_num]

    ################################################
    # This section randomizes the parts of speech in a sentence structure
    # Also keeps track of how things were shuffled
    rand_sentence_structure = deepcopy(sentence_structure)
    rand_sentence = []
    rand_index = []

    for x in xrange(0, len(rand_sentence_structure)):
        rand_sentence_structure[x] = [rand_sentence_structure[x], x]

    rand.shuffle(rand_sentence_structure)

    for x in xrange(0, len(rand_sentence_structure)):
        rand_index.append(rand_sentence_structure[x][1])
        rand_sentence_structure[x] = rand_sentence_structure[x][0]
    remaining_pos = len(sentence_structure)
    remaining_syll = syll_count
    #################################################

    #################################################
    # Generates word by word for the randomized sentence structure
    # num_tries_before_retry is the "check" for infinite loops
    # If a line cannot be generated after 1000 tries, it tries a new structure/words
    num_tries_before_retry = 20
    for generate_word in rand_sentence_structure:
        wordTuple = generate_word()
        word = wordTuple.text
        word_syll = wordTuple.syllable_count
        if remaining_pos == 1:
            while word_syll != remaining_syll:
                if num_tries_before_retry < 0:
                    return generate_line(syll_count, theme)
                wordTuple = generate_word()
                word = wordTuple.text
                word_syll = wordTuple.syllable_count
                num_tries_before_retry -= 1
        else:
            while word_syll > (remaining_syll - remaining_pos + 1):
                wordTuple = generate_word()
                word = wordTuple.text
                word_syll = wordTuple.syllable_count

        remaining_syll -= word_syll
        remaining_pos -= 1
        rand_sentence.append(word)
    #################################################

    # Finally, we fix the ordering back to the original and return it
    sentence = range(len(rand_sentence))
    for x in xrange(0, len(rand_sentence)):
        sentence[rand_index[x]] = rand_sentence[x]

    return " ".join(sentence).encode('utf-8')
