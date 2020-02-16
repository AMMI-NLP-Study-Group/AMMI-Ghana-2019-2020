from typing import Set
import re
from utils import *


d = read_file("./Data/worked_example.train")
d_test = read_file("./Data/worked_example.test",is_train=False)

vocabulary = get_vocab(d)

count_table = get_count_table(d, vocabulary)
x_text = get_count_table(d_test,vocabulary)

p_c = get_prior(d)
pwc = get_likelihood(vocabulary, count_table, d["output"])
print(count_table)

result = []
for index,classes in enumerate(sorted(set(d['output']))):
    pc_i = p_c[classes]
    product = 1
    for i in range(len(x_text[0])):
        if x_text[0][i] != 0:
            pwc_i = pwc[index][i]**x_text[0][i]
            product = product * (pwc_i)
    result.append(product*pc_i)


print(result.index(max(result)))
