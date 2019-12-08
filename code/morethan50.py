from shutil import copyfile
import os

for filename in os.listdir("data/25good"):
    count = 0
    path = "data/25good/"+filename
    input_file = open(path)
    for line in input_file:
        count +=1
    input_file.close()
    if count >100:
        os.remove(path)
        #dest = "data/25good/" + filename
        #copyfile(path, dest)