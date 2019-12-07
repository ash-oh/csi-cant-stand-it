from collections import Counter
import nltk
import os
bad = ""
for filename in os.listdir("data/olddata/character/bad"):
    path = "data/olddata/character/bad/" + filename
    content = ""
    with open (path, 'r' ) as f:
        content = f.read()
    f.close()
    bad = bad + " " + content
good = ""
for filename in os.listdir("data/olddata/character/good"):
    path = "data/olddata/character/good/" + filename
    content = ""
    with open (path, 'r' ) as f:
        content = f.read()
    f.close()
    good = good + " " + content


lower_case = bad.lower()
token = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(token)
counts = Counter (tag for word, tag in tags)
print(counts)
print (len(token))

lower_case = good.lower()
token = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(token)
counts = Counter (tag for word, tag in tags)
print(counts)
print (len(token))