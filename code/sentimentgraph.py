import matplotlib.pyplot as plt
from textblob import TextBlob
import os



bad_pol =[]
bad_sub = []

good_pol =[]
good_sub =[]

for file in os.listdir("data/characters/bad"):
    path = "data/characters/bad/" +file
    with open(path) as f:
        doc = f.read().rstrip("\n")
                                     
    blob = TextBlob(doc)       
    bad_pol.append(blob.sentiment.polarity)
    bad_sub.append(blob.sentiment.subjectivity)
for file in os.listdir("data/characters/good"):
    path = "data/characters/good/" +file
    with open(path) as f:
        doc = f.read().rstrip("\n")
                                     
    blob = TextBlob(doc)       
    good_pol.append(blob.sentiment.polarity)
    good_sub.append(blob.sentiment.subjectivity)


print (len (good_pol))
print(len(bad_pol))
plt.plot(good_pol, good_sub, 'bs')
plt.plot(bad_pol, bad_sub, 'ro')
plt.xlabel('polarity')
plt.ylabel('subjectivity')
plt.show()