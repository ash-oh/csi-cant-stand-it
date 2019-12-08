import os

for file in os.listdir("data/clean"):
    path = "data/clean/" + file
    print(file)
    input_file = open(path)
#not the best method of extracting characters because will split in the middle of lines if there is :
#if time will explore again using regex
    for line in input_file:
        if ':' in line:
            name = line.split(':',1)[0]
            if any(c.islower() for c in name) and ('Sound' not in name) and ('(' not in name):
                filename = name.strip()
                filename = filename.lower()
                filename = filename.oreplace(" ","_")
                filename = filename.replace("/","-")

                name = name + ':'
                name = name.lstrip()

                output_file = open("data/characters/"+filename + ".txt", 'a+')

                line = line.replace(name, '')
                #line = line.replace("&quot;", "")
                line = line.lstrip()
                output_file.write(line)

    input_file.close()
    output_file.close()



