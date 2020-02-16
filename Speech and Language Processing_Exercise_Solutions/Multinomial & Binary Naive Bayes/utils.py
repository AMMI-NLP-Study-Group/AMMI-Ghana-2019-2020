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


def get_prior(d):
        y = d['output']
        uniq_y = set(y)
        total = len(y)
        final_prior = {}
        for item in uniq_y:
                tmp = [x for x in y if x == item]
                final_prior[item] = len(tmp)/total

        return final_prior

def get_likelihood(vocabulary, count_table, labels):
        s = sorted(list(set(labels)))
        # print(s)
        result = [[0 for i in range(len(vocabulary))] for j in range(len(s))]
        for c_idx, c in enumerate(s):
                # Tc = 0
                # for i, row in enumerate(count_table):
                #         if labels[i]==c:
                #                 Tc+=sum(row)
        
                Tc = sum([sum(row) for i,row in enumerate(count_table) if labels[i]==c])
                for word in vocabulary.keys():
                        word_idx = vocabulary[word]
                        c_wc = sum([count_table[i][word_idx] for i in range(len(labels)) if labels[i]==c]) 
                        result[c_idx][word_idx] = (c_wc+1)/(Tc+len(vocabulary))
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