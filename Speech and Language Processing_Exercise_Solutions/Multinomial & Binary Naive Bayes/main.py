from typing import Set
import re
from utils import *


d = read_file("./Data/worked_example.train")

vocabulary = get_vocab(d)

count_table = get_count_table(d, vocabulary)

p_c = get_prior(d)
pwc = get_likelihood(vocabulary, count_table, d["output"])
print(count_table)