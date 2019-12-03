import re
import os

characters = {}

for file in os.listdir("data/transcripts"):
    path = "data/transcripts/" + file
    print(file)
    input_file = open(path)
    for line in input_file:
        parts = line.split(":",1)
        if len(parts) ==2 :
            parts[0] = parts[0].lower()
            parts[0] = parts[0].replace(" ","_")
            parts[0] = parts[0].replace("/","-")
            if parts[0] in characters:
                characters[parts[0]].append(parts[1])
            else:
                characters[parts[0]] = [parts[1]]

for name in characters:
    file = open("data/char/"+name+ ".txt", 'a+')
    for line in characters[name]:
        file.write(line)
    file.close()    



