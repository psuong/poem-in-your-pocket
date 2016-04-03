from line_generate import generate_line

# Generate our 3 haiku lines with the syllable count as arguments
line1 = generate_line(5)
line2 = generate_line(7)
line3 = generate_line(5)

# Print the haiku!
print "%s\n%s\n%s" % (line1,line2,line3)