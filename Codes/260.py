import re

def text_match_wordz_middle(text):
    patterns = r'\Bz\B'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match_wordz_middle("The quick brown fox jumps over the lazy dog."))