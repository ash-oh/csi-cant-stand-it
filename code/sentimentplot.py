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


label = ["Non-Murderer", "Murderer"]
data = [good_pol, bad_pol]
data2 = [good_sub,bad_sub]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

# plot polarity plot
axes[0].boxplot(data)
axes[0].set_title('Polarity')
axes[0].set_ylabel("Polarity")


# plot Subjectivity plot
axes[1].boxplot(data2)
axes[1].set_title('Subjectivity')
axes[1].set_ylabel("Subjectivity")

plt.setp(axes, xticks=[1,2],
         xticklabels=label)

plt.show()



