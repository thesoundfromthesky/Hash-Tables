import random
import re

# Read in all the words in one go
# with open("input.txt") as f:
with open("./applications/markov/test.txt") as f:
    words = f.read()
    word_dict={}
    word_list = words.split()
    word_start={}
    word_end={}
    for w in word_list:
        if w not in word_dict:
            escape_w=re.escape(w)
            rxp_start= rf"(?<={escape_w}\s)[\w\-,\"';:!?.()]+(?=\s?)"
            rxp = rf"(?<={escape_w}\s)[\w\-,\"';:!?.()]+(?=\s?)"
            word_dict[w] = re.findall(rxp, words)
    
    word_keys = list(word_dict.keys())
    nxt = random.choice(word_keys)
    st=""
    while nxt:
         if not word_dict[nxt]:
             break
         nxt = random.choice(word_dict[nxt])
         st = " ".join([st, nxt])

    print(st)


# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences
