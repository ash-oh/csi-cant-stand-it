import os

for file in os.listdir("data/transcripts"):
	path = "data/transcripts/" + file
	input_file = open(path)

	for line in input_file:
		if ':' in line:
			name = line.split(':')[0]
			if any(c.islower() for c in name) and ('Sound' not in name) and ('(' not in name):
				filename = name.strip()
				filename = filename.replace(" ","_")

				name = name + ':'
				name = name.lstrip()

				output_file = open("data/character/"+filename + ".txt", 'a+')
				
				line = line.replace(name, '')
				line = line.replace("&quot;", "")
				line = line.lstrip()
				output_file.write(line)

	input_file.close()
	output_file.close()



