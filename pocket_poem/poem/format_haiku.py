def format_haiku_lines(haiku_content):
    """
    Formats the Haiku to look much more appealing.
    :param haiku_content: list
    """
    list_of_lines = []
    for line in haiku_content:
        list_of_lines.append(line[0].upper() + line[1:len(line)])
    return list_of_lines
