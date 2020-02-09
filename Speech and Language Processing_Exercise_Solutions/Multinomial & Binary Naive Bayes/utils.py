from typing import Set
import re

def tokenize(text: str) -> Set[str]:
    text = text.lower()                         # Convert to lowercase,
    all_words = re.findall("[a-z0-9']+", text)  # extract the words, and
    return all_words                       # remove duplicates.

# assert tokenize("Data Science 01, is & _ is science") == {"data", "science", "is"}


import os
from collections import Counter

def get_count_table(d, vocabulary):
    X = d["input"]
    v = len(vocabulary)
    result = []
    for sentence in X:
        sentence = tokenize(sentence)
        counter = Counter(sentence)
        vector = [0 for i in range(v)]
        for word in counter.keys():
            vector[vocabulary[word]] = counter[word]
        result.append(vector)

    return result




def get_vocab(d):
    final_d = {}
    index_counter = 0
    for i,  _ in enumerate(d['input']):
        x = tokenize(d['input'][i])
        for x_i in x:
            if not x_i in final_d:
                final_d[x_i] = index_counter
                index_counter += 1
    return final_d


def read_file(file_path):
        x = []
        y = []
        lines = open(file_path).readlines()

        for i in range(len(lines)):
                reading = lines[i].strip().split(';')
                x.append(reading[0])
                y.append(reading[1])

        return {'input':x, 'output': y}



d = read_file("./Data/worked_example.train")

vocabulary = get_vocab(d)

get_count_table(d, vocabulary)
