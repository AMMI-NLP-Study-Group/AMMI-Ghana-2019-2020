from collections import Counter

def question38(Text):
    words = Text.split()
    word_counts = Counter(words)
    sorted_vocab = sorted(word_counts, key=word_counts.get, reverse=True)
    # create int_to_vocab dictionaries
    unigram = {word: (word_counts[word]+1)/(len(words)+len(set(sorted_vocab))) for word in sorted_vocab}

    return unigram

Text = "The workplace has changed: as technology continues to rapidly transform industries and jobs, staying relevant and competitive requires continuously building completely new skill sets. But we are here to help you adapt to the demands of the modern workplace and the lifestyle of the modern worker. Read up on what modular education is and how it can benefit you!"
print(question38(Text))

