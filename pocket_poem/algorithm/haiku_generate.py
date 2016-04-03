# coding=utf-8
from line_generate import generate_line
from ginger.ginger_python2 import get_ginger_result


def grammar_check(text):
    if len(get_ginger_result(text[0].upper() + text[1:])['LightGingerTheTextResult']) == 0:
        return True
    else:
        return False


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

    # Print the haiku!
    print "%s\n%s\n%s" % (line1, line2, line3)
