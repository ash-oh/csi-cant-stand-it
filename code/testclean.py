import os
import re


path = "data/transcripts/S5-Ep3.txt"
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
    
    content = re.sub ("\[.*\]", "", content)
    content = re.sub ("^[A-Z].*", "", content)
    #content = re.sub("[A-Z][A-Z][A-Z].*", "", content)
    content = re.sub ("&quot;", "'", content)
    content = re.sub ("\n\s*[A-Z][A-Z]+.*", "", content)
    content = re.sub ("\n\d.*","", content)

with open (path, 'w' ) as f:
    f.write(content)






