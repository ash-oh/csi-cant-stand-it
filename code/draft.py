import re
import nltk
import csv
import numpy as np
from textblob import TextBlob



#GLOBAL STUFF

print("[polarity, subjectivity, valence, arousal, dominance]")


with open('Ratings_Warriner_et_al.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file)
	line_count = 0
	d = {}
	for row in csv_reader:
		d[row[1]] = [row[2],row[5],row[8]] #valence, arousal, dominance in order. 


sample = []
data = []

#functions
def warriner_rating(alltokens):
	count = 0
	ratings = [0,0,0]

	for word in alltokens:
		if word in d.keys():
			count += 1
			newrating = [float(i) for i in d[word]] #['7','2','1'] --> [7,2,1]
			ratings = [sum(x) for x in zip(ratings,newrating)] #elementwise addition.
	ratings =[x/count for x in ratings]
	return ratings

def textblob_sentiment(text):
	obj = TextBlob(text)
	return obj.sentiment


# SHOULD BE IN FOR LOOP LATER TO LOOP THORUGH ALL SCRIPT
f = open("Husband.txt")
text = f.read().rstrip()
text = re.sub("\n", " ", text)

text = text.lower()

#textblob
sentiment = textblob_sentiment(text)
sample.append(sentiment[0])
sample.append(sentiment[1])

alltokens = nltk.word_tokenize(text)
ratings = warriner_rating(alltokens)

sample.append(ratings[0])
sample.append(ratings[1])
sample.append(ratings[2])

print(sample)

#data.append(sample)
#print(data)



