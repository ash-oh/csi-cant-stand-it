from nltk import FreqDist
import glob
from nltk.corpus import stopwords
import math
import re
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn import metrics
import csv
import numpy as np

stops = stopwords.words('english')
stops.extend([",", ".", "!", "?", "'", '"', "I", "i", "n't", "'ve", "'d", "'s"])

allwords = []

## read in nonmurderer lines and save as list
goodwords = []
allgood = glob.glob("/Users/JessBolduc/Documents/BostonCollege/SeniorYear/NaturalLanguageProcessing/csi-cant-stand-it-master/data/characterswtesting/good/*")
for filename in allgood:
    f = open(filename)
    toextend = []
    for line in f:
        words = line.rstrip().lower().split()
        toextend.extend(list(set([w for w in words if not w in stops])))
    f.close()
    goodwords.append(list(set(toextend)))
    allwords.extend(list(set(toextend)))

## read in murderer lines and save as list
badwords = []
allbad = glob.glob("/Users/JessBolduc/Documents/BostonCollege/SeniorYear/NaturalLanguageProcessing/csi-cant-stand-it-master/data/characterswtesting/bad/*")
for filename in allbad:
    f = open(filename)
    toextend = []
    for line in f:
        words = line.rstrip().split()
        toextend.extend(list(set([w for w in words if not w in stops])))
    f.close()
    badwords.append(list(set(toextend)))
    allwords.extend(list(set(toextend)))


with open('Ratings_Warriner_et_al.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file)
	line_count = 0
	d = {}
	for row in csv_reader:
		d[row[1]] = [row[2],row[5],row[8]] #valence, arousal, dominance in order. 
def warriner_rating(alltokens):
	count = 0
	ratings = []
	maxValence = 0
	maxArousal = 0
	maxDominance = 0
	minValence = 10
	minArousal = 10
	minDominance = 10

	for word in alltokens:
		if word in d.keys():
			newrating = [float(i) for i in d[word]] #['7','2','1'] --> [7,2,1]

			if newrating[0] > maxValence:
				maxValence = newrating[0]
			if newrating[1] > maxArousal:
				maxArousal = newrating[1]
			if newrating[2] > maxDominance:
				maxDominance = newrating[2]

			if newrating[0] < minValence:
				minValence = newrating[0]
			if newrating[1] < minArousal:
				minArousal = newrating[1]
			if newrating[2] < minDominance:
				minDominance = newrating[2]

			count += 1
			#ratings = [sum(x) for x in zip(ratings,newrating)] #elementwise addition.

	#ratings =[x/count for x in ratings]

	ratings.append(maxValence)
	ratings.append(maxArousal)
	ratings.append(maxDominance)
	ratings.append(minValence)
	ratings.append(minArousal)
	ratings.append(minDominance)

	return ratings

def halfandhalf(review):
    leng=int(len(review)/2)
    firsthalf=review[0:leng]
    secondhalf=review[leng:]
    difference = []
    w1=warriner_rating(firsthalf)
    w2=warriner_rating(secondhalf)
    for i in range(len(w1)):
        difference.append(w2[i]-w1[i])
    return difference


list1=["heated", "cold", "taco", "cheese","pizza", "kill", "murder","angry", "mad", "irate"]
print(list1)
print(halfandhalf(list1))



## Get the 1000 most frequent words to use as features

wfreq = FreqDist(allwords)
top1000 = wfreq.most_common(1000)

training = []
traininglabel = []


for p in goodwords:
    vec = []
    for t in top1000:
        if t[0] in p:
            vec.append(1)
        else:
            vec.append(0)
    rat=halfandhalf(p)
    vec=[]
    for item in rat:
        vec.append(item)
    
    training.append(vec)
    traininglabel.append(1)

for n in badwords:
    vec = []
    for t in top1000:
        if t[0] in n:
            vec.append(1)
        else:
            vec.append(0)
    vec=[]
    rat=halfandhalf(n)
    for item in rat:
        vec.append(item)
    training.append(vec)
    traininglabel.append(0)
#TESTING

testing = []
testinglabel = []

testdata = glob.glob("/Users/JessBolduc/Documents/BostonCollege/SeniorYear/NaturalLanguageProcessing/csi-cant-stand-it-master/data/characterswtesting/testing/*")
for filename in testdata:
    print(filename)
    rw = []
    f = open(filename)
    filepolarity = re.sub(r"^(pos|neg)", r"\1", filename)

    for line in f:
        words = line.rstrip().lower().split()
        for w in words:
            rw.append(w)
        #rw.extend(words)
        #rw.extend(list(set([w for w in words if not w in stops])))
    f.close()
    vec = []
    for t in top1000:
        if t[0] in rw:
            vec.append(1)
        else:
            vec.append(0)
    vec=[]
    rat=halfandhalf(rw)
    print(rat)
    for item in rat:
        vec.append(item)
    testing.append(vec)
    print(len(vec))
    if  "neg" in filename:
        testinglabel.append(0)
    else:
        testinglabel.append(1)


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(training, traininglabel)
predicted = clf.predict(testing)
print("Accuracy of Multi-Layer Perceptron")
print(metrics.classification_report(testinglabel, predicted))


       


