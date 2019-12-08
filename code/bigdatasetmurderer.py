
import numpy as np
import matplotlib.pyplot as plt
import gensim
import re
import nltk
import os
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
directory = "/Users/JessBolduc/Documents/BostonCollege/SeniorYear/NaturalLanguageProcessing/csi-cant-stand-it-master/data/characters/bad"
folder= os.fsencode(directory)
alltextbad = ''
badguys = {}
count = 0
for file in os.listdir(folder):
    filename = directory + "/" + os.fsdecode(file)
    f = open(filename)
    # read in the whole file into a string called alltextbad
    temp = f.read()
    alltextbad = alltextbad + " "+ temp
    alltextbad=alltextbad[:-1]
    #murdergraph prep
    temp=re.sub("\n", " ", temp)
    templist = nltk.sent_tokenize(temp)
    templist2 =[]
    for item in templist:
        templist2.append(nltk.word_tokenize(item))
    badguys[count]=templist2
    count +=1
    f.close()
# replace all "\n" in the string alltext with a space (i.e, " ")
alltextbad=re.sub("\n", " ", alltextbad)

# break the string into a list of sentences with nltk.sent_tokenize
badlistt = nltk.sent_tokenize(alltextbad)

# break each sentence into a list of tokens and store list of lists in badtoksents
badtoksents =[]
for item in badlistt:
    badtoksents.append(nltk.word_tokenize(item))
 
directory = "/Users/JessBolduc/Documents/BostonCollege/SeniorYear/NaturalLanguageProcessing/csi-cant-stand-it-master/data/characters/good"
folder= os.fsencode(directory)
alltextgood = ''
count = 0
goodguys = {}
for file in os.listdir(folder):
    filename = directory + "/" + os.fsdecode(file)
    f = open(filename)
    # read in the whole file into a string called alltextgood
    temp = f.read()
    alltextgood = alltextgood + " "+ temp
    alltextgood=alltextgood[:-1]
    #murdergraph prep
    temp=re.sub("\n", " ", temp)
    templist = nltk.sent_tokenize(temp)
    templist2 =[]
    for item in templist:
        templist2.append(nltk.word_tokenize(item))
    goodguys[count]=templist2
    count +=1
    f.close()
# replace all "\n" in the string alltext with a space (i.e, " ")
alltextgood=re.sub("\n", " ", alltextgood)

# break the string into a list of sentences with nltk.sent_tokenize
goodlistt = nltk.sent_tokenize(alltextgood)

# break each sentence into a list of tokens and store list of lists in goodtoksents
goodtoksents =[]
for item in goodlistt:
    goodtoksents.append(nltk.word_tokenize(item))
alltoksents = goodtoksents + badtoksents
#model = gensim.models.Word2Vec(alltoksents, size=100, window=5, min_count=1, workers=4)
bigmodel = gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300-SLIM.bin", binary=True)
print("model built!")

#mean vector for each character
vectors = []
for i in range(len(badguys)):
    character = badguys[i]
    characterwords=[]
    for sentence in character:
        for word in sentence:
            if word in bigmodel:
                characterwords.append(word)
    vectors.append(np.mean(bigmodel[characterwords], axis =0))


badblue = len(vectors)
for i in range(len(goodguys)):
    character = goodguys[i]
    characterwords=[]
    for sentence in character:
        for word in sentence:
            if word in bigmodel:
                characterwords.append(word)
    vectors.append(np.mean(bigmodel[characterwords], axis =0))
    print("in here")
    
# Do the PCA to reduce to 2 dimensions
pca = PCA(n_components=2, whiten=True)
vectors2d = pca.fit(vectors).transform(vectors)

i = 0
for point in vectors2d:
    if i > badblue:
        plt.scatter(point[0], point[1], facecolors='none', edgecolors='r',zorder=1)
    else:
        plt.scatter(point[0], point[1], facecolors ='none', edgecolors='b',zorder=2)
    i += 1
    

plt.show()






