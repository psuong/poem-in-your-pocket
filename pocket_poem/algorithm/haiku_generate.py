# coding=utf-8
from line_generate import generate_line


def generate_haiku(theme=None):
    # Generate our 3 haiku lines with the syllable count as arguments
    line1 = generate_line(5, theme)
    line2 = generate_line(7, theme)
    line3 = generate_line(5, theme)

    # Print the haiku!
    print "%s\n%s\n%s" % (line1, line2, line3)
