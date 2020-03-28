import os
import pickle
import string
from random import choice as randomise
from random import randrange
import api

file_path = os.path.join(os.path.dirname(api.__file__), 'word_list.pkl')

with open(file_path, 'rb') as f:
    WORD_LIST = pickle.load(f)

SYMBOLS = string.punctuation


def create_pass(symbols, register, readable, numeric, length):
    length = int(length)
    result = []
    for i in range(length):
        if readable:
            word = randomise(WORD_LIST)
            result.append(word)
        else:
            result.append(randomise(string.ascii_lowercase))

    percent_change = int((randrange(2, 6, 1) * 0.1) * length)

    if symbols:
        for i in range(percent_change):
            idx = randrange(0, length)
            symb = randomise(SYMBOLS)
            if readable:
                result[idx] = symb + result[idx] if randomise([0, 1]) else \
                    result[idx] + symb
            else:
                result[idx] = symb

    if register:
        if readable:
            result = [word.capitalize() for word in result]
        else:
            for i in range(percent_change):
                idx = randrange(0, length)
                result[idx] = result[idx].upper()

    if numeric:
        for i in range(percent_change):
            idx = randrange(0, length)
            numer = str(randomise(range(0, 101)))
            if readable:
                result[idx] = numer + result[idx] if randomise([0, 1]) else \
                    result[idx] + numer
            else:
                result[idx] = numer

    return ''.join(result)
