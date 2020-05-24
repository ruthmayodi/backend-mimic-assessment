#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Ruth Mayodi, ruthmayodi, with the help of Howard Post"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    f = open(filename, "r")
    book = f.read()
    f.close()
    words = book.split()
    word_dict = {'': words[0]}
    for index in range(len(words)-1):
        #if words[index] in word_dict.keys():
        word_dict.setdefault(words[index], []).append(words[index + 1])
        #else:
             #word_dict[words[index]] = words[index + 1]
        
            
    return word_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    num = 0 
    print(mimic_dict[start_word])
    results = mimic_dict[start_word] + " "
    next_word = mimic_dict[start_word]
    while num <= 200:
        rando = random.choice(mimic_dict[next_word])
        if len(results) + len(rando) < 70:
            results += rando + " "
        else:
            print(results, "\n")
            results = rando + " "
        if rando in mimic_dict:
            next_word = rando
        else:
            next_word = start_word
        num += 1


    pass


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
