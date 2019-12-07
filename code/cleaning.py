import os
import re
content = ""
for filename in os.listdir("data/transcripts"):
    path = "data/transcripts/" + filename
    new = "data/clean/"+ filename
    content = ""
    with open (path, 'r' ) as f:
        content = f.read()
        content = re.sub ("<p><strong>End</strong></p>", "pstrongEndstrongp", content)
        content = re.sub("<.*?>", "",content)
        content = re.sub ("pstrongEndstrongp.*","", content, flags=re.S)
        content = re.sub ("<meta name.*?\(\{\}\);", "", content,flags=re.S )
        content = re.sub ("\(.*\):", ":", content)
        content = re.sub ("\(.*\)", "", content)
        content = re.sub("\(.*", "", content)
        
        content = re.sub ("\[.*\n*.*\]", "", content)
        content = re.sub ("\[.*", "", content)
        content = re.sub ("^[A-Z].*", "", content)
        #content = re.sub("[A-Z][A-Z][A-Z].*", "", content)
        content = re.sub ("&quot;", "'", content)
        content = re.sub ("\n\s*[A-Z][A-Z]+.*", "", content)
        content = re.sub ("\n\d.*","", content)
        


    with open (new, 'w' ) as f:
        f.write(content)





