import sys
punctuations = '''!()-[]{};:'",.?'''


def text_analyzer(*args):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if len(args) > 1:
        exit("ERROR")
    if not args:
        text = input("What is the text to analyse?\n")
    else:
        text = args[0]
    i, upper, lower, punct, spaces = 0, 0, 0, 0, 0
    while i < len(text):
        if text[i].isupper():
            upper += 1
        elif text[i].islower():
            lower += 1
        elif text[i] in punctuations:
            punct += 1
        elif text[i] == ' ':
            spaces += 1
        i += 1
    print("The text contain", i, "characters:\n")
    print("-", upper, "upper letters\n")
    print("-", lower, "lower letters\n")
    print("-", punct, "punctuation marks\n")
    print("-", spaces, "spaces")
