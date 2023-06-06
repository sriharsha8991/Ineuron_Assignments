# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:32:00 2023

@author: sriharsha
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def count_pos_tags(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform Part-of-Speech (POS) tagging on the words
    tagged_words = pos_tag(words)

    # Initialize counts
    counts = {
        'Noun': 0,
        'Verb': 0,
        'Pronoun': 0,
        'Adjective': 0
    }

    # Iterate through tagged words and count the occurrences of each POS tag
    for word, tag in tagged_words:
        if tag.startswith('NN'):  # Noun
            counts['Noun'] += 1
        elif tag.startswith('VB'):  # Verb
            counts['Verb'] += 1
        elif tag.startswith('PRP'):  # Pronoun
            counts['Pronoun'] += 1
        elif tag.startswith('JJ'):  # Adjective
            counts['Adjective'] += 1

    return counts


# Test case 1 - A simple phrase
phrase1 = "The quick brown fox jumps over the lazy dog."
result1 = count_pos_tags(phrase1)
print(result1)  # {'Noun': 2, 'Verb': 1, 'Pronoun': 0, 'Adjective': 2}

# Test case 2 - A longer paragraph
paragraph2 = "John is a software engineer who loves programming. He works diligently on his projects and enjoys solving complex problems using innovative solutions."
result2 = count_pos_tags(paragraph2)
print(result2)  # {'Noun': 4, 'Verb': 3, 'Pronoun': 2, 'Adjective': 3}
