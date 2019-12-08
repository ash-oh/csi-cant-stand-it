import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from textblob import TextBlob
import os



bad_pol =[]
bad_sub = []

good_pol =[]
good_sub =[]

detect_pol =[]
detect_sub = []

for file in os.listdir("data/characters/bad"):
    path = "data/characters/bad/" +file
    with open(path) as f:
        doc = f.read().rstrip("\n")
                                     
    blob = TextBlob(doc)       
    bad_pol.append(blob.sentiment.polarity)
    bad_sub.append(blob.sentiment.subjectivity)
for file in os.listdir("data/good"):
    path = "data/good/" +file
    with open(path) as f:
        doc = f.read().rstrip("\n")
                                     
    blob = TextBlob(doc)       
    good_pol.append(blob.sentiment.polarity)
    good_sub.append(blob.sentiment.subjectivity)

for file in os.listdir("data/detective"):
    path = "data/detective/" +file
    with open(path) as f:
        doc = f.read().rstrip("\n")
                                     
    blob = TextBlob(doc)       
    detect_pol.append(blob.sentiment.polarity)
    detect_sub.append(blob.sentiment.subjectivity)


data = [good_pol, bad_pol, detect_pol]
data2 = [good_sub,bad_sub, detect_pol]

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(4, 4)
fig.suptitle("Sentiment Analysis")

#plot graph
f_ax1 = fig.add_subplot(gs[:,0:3])
f_ax1.plot(good_pol, good_sub, 'bs', label = "Non-Murderer (1)")
f_ax1.plot(bad_pol, bad_sub, 'ro', label = "Murderer (2)")
f_ax1.plot(detect_pol, detect_sub, 'g^', label = "Detective (3)")
f_ax1.set_xlabel("Polarity")
f_ax1.set_ylabel("Subjectivity")
f_ax1.legend()

#plot polarity
f_ax2 = fig.add_subplot(gs[0:2,3:])
f_ax2.boxplot(data)
f_ax2.set_ylabel("Polarity")


# plot Subjectivity
f_ax3 = fig.add_subplot(gs[2:,3:])
f_ax3.boxplot(data2)
f_ax3.set_ylabel("Subjectivity")


plt.show()



