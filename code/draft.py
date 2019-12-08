import re
import nltk
import csv
import numpy as np
from textblob import TextBlob
import os


#GLOBAL STUFF

print("[polarity, subjectivity, valence, arousal, dominance]")
with open('Ratings_Warriner_et_al.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file)
	line_count = 0
	d = {}
	for row in csv_reader:
		d[row[1]] = [row[2],row[5],row[8]] #valence, arousal, dominance in order. 
gooddata = []
baddata = []


#functions
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

def textblob_sentiment(text):
	obj = TextBlob(text)
	return obj.sentiment


# SHOULD BE IN FOR LOOP LATER TO LOOP THORUGH ALL SCRIPT



def analyze_script(goodorbad, trainingdata):
	directory = "/Users/david/Desktop/csi/data/characters/"
	directory += goodorbad
	folder= os.fsencode(directory)
	
	for file in os.listdir(folder):
	    filename = directory + "/" + os.fsdecode(file)
	    f = open(filename)

	    text = f.read().rstrip()
	    text = text.lower()

	    firstsample = []
	    secondsample = []
	    listoftest = text.split("\n")
	    secondhalf = "\n".join(listoftest[(len(listoftest)//2):])
	    firsthalf = "\n".join(listoftest[:(len(listoftest)//2)])
	    initialsentiment = textblob_sentiment(firsthalf)
	    firstsample.append(initialsentiment[0])
	    firstsample.append(initialsentiment[1])
	    endingsentiment = textblob_sentiment(secondhalf)
	    secondsample.append(endingsentiment[0])
	    secondsample.append(endingsentiment[1])
	    firsttoken = nltk.word_tokenize(firsthalf)
	    secondtoken = nltk.word_tokenize(secondhalf)
	    firstrating = warriner_rating(firsttoken)
	    firstsample += firstrating
	    secondrating = warriner_rating(secondtoken)
	    secondsample += secondrating

	    difference = [0]*len(firstsample)
	    for i in range(len(firstsample)):
	    	 difference[i] = firstsample[i] - secondsample[i]

	    
	    last10lines = "\n".join(text.split("\n")[-10:])



	    sentiment = textblob_sentiment(last10lines) #or text
	    sample = []
	    sample.append(sentiment[0])
	    sample.append(sentiment[1])
	    alltokens = nltk.word_tokenize(last10lines) #or text
	    ratings = warriner_rating(alltokens)
	    sample += ratings
	    trainingdata.append(sample)
	    #trainingdata.append(difference)
	    f.close()
	    


def calculate_avg_score(data):
	numOfScript = 0
	avg_score = [0,0,0,0,0,0,0,0]
	for d in data:
		numOfScript += 1
		for i in range(len(avg_score)):
			avg_score[i] += d[i]
	for j in range(len(avg_score)):
		avg_score[j] /= numOfScript
	avg_score = [round(x,5) for x in avg_score]
	return avg_score



####################################
analyze_script("bad", baddata)
analyze_script("good", gooddata)

bad_avg_score = calculate_avg_score(baddata)
good_avg_score = calculate_avg_score(gooddata)


print("avg score for bad:", bad_avg_score)
print("avg score for good:", good_avg_score)


for data in gooddata:
	data.append(1)
for data in baddata:
	data.append(0)

data = gooddata + baddata
dataset = np.array(data)


#print(dataset)

 


#######MACHINE LEARNING MODEL#############

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_validate
from sklearn import metrics




def classify(dataset):
	(numSamples, numFeatures) = dataset.shape
	data = dataset[:,range(numFeatures-1)].reshape((numSamples, numFeatures-1))
	labels = dataset[:, numFeatures-1].reshape((numSamples,))
	(numSamples, numFeatures) = data.shape
	print(labels)
	print(len(labels))
	print(sum(labels))
	print("majority baseline:", sum(labels)/len(labels))


	print(" ")
	print("GaussianNB RESULTS")
	gnb = GaussianNB()
	scoring_metrics = ['accuracy', 'precision', 'recall', 'f1']
	# Let's train a model with 5-fold cross validation.
	scores = cross_validate(gnb, data, labels, cv=10, scoring=scoring_metrics)
	# Then we print out each of the metrics for each of the 5 folds.
	for score_name, score_value in scores.items():
	    print(score_name, score_value.mean())
	print(" ")
	print("KN results")

	from sklearn.neighbors import KNeighborsClassifier
	neigh = KNeighborsClassifier(n_neighbors=3)
	knn_scores = cross_validate(neigh, data, labels, cv=10, scoring= scoring_metrics)
	for score_name, score_value in knn_scores.items():
	    print(score_name, score_value.mean())
	print(" ")
	print("SVM RESULTS")
	from sklearn.svm import LinearSVC
	svmclf = LinearSVC()
	svm_scores = cross_validate(svmclf, data,labels, cv=10, scoring=scoring_metrics)
	for score_name, score_value in svm_scores.items():
		print(score_name, score_value.mean())

	from sklearn.linear_model import LogisticRegression
	logclf = LogisticRegression(random_state = 0)
	log_scores = cross_validate(logclf, data, labels, cv=10, scoring=scoring_metrics)
	for score_name, score_value in log_scores.items():
		print(score_name, score_value.mean())



classify(dataset)


####PLOTTTING STUFF #######


import numpy as np
import matplotlib.pyplot as plt


gooddata = np.array(gooddata)
baddata = np.array(baddata)

goodArousal = gooddata[:,2]
goodValence = gooddata[:,3]

badArousal = baddata[:,2]
badValence = baddata[:,3]

plt.xlabel("Arousal")
plt.ylabel("Valence")
plt.title("Arousal vs Valence of Characters")
plt.scatter(goodArousal, goodValence, c='r', label = "innocent")
plt.scatter(badArousal, badValence, label ="criminal")
plt.legend()
plt.show()



