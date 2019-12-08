import os
small = 0
large = 0
for filename in os.listdir("data/characters/good"):
    count = 0
    path = "data/characters/good/"+filename
    input_file = open(path)
    for line in input_file:
        count +=1
    input_file.close()
    if count <=2:
        os.remove(path)
        
