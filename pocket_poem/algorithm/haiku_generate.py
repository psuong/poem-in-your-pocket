# coding=utf-8
from line_generate import generate_line
from ginger.ginger_python2 import get_ginger_result


def grammar_check(text):
    if len(get_ginger_result(text[0].upper() + text[1:])['LightGingerTheTextResult']) == 0:
        return True
    else:
        return False

def starts_with_vowel(word):
    if word[0] in "aeiou":
        return True
    return False

def replace_a_an(line):
    list_line = line.split(" ")
    for i in xrange(0,len(list_line)):
        if list_line[i] == "a" and starts_with_vowel(list_line[i+1]):
            list_line[i] = "an"
        if list_line[i] == "an" and (not starts_with_vowel(list_line[i+1])):
            list_line[i] = "a"

def generate_haiku(theme=None):
    # Generate our 3 haiku lines with the syllable count as arguments
    line1 = generate_line(5, theme)
    while not grammar_check(line1):
        line1 = generate_line(5, theme)
    line2 = generate_line(7, theme)
    while not grammar_check(line2):
        line2 = generate_line(7, theme)
    line3 = generate_line(5, theme)
    while not grammar_check(line3):
        line3 = generate_line(5, theme)
    
    replace_a_an(line1)
    replace_a_an(line2)
    replace_a_an(line3)
    

    # Print the haiku!
    # print "%s\n%s\n%s" % (line1, line2, line3)
    return line1, line2, line3
