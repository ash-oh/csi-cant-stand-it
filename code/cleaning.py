import os
import re
content = ""
for filename in os.listdir("data/transcripts"):
    path = "data/transcripts/" + filename
    content = ""
    with open (path, 'r' ) as f:
        content = f.read()
        content = re.sub ("<p><strong>End</strong></p>", "pstrongEndstrongp", content)
        content = re.sub("<.*?>", "",content)
        #content = re.sub ("data-full-width.*", "", content)
        #content = re.sub ("data-ad-client=.*", "", content)
        #content = re.sub ("data-ad-slot=.*", "", content)
        #content = re.sub ("\(adsbygoogle =.*", "", content)
        content = re.sub ("pstrongEndstrongp.*","", content, flags=re.S)
        content = re.sub ("<meta name.*?\(\{\}\);", "", content,flags=re.S )
        content = re.sub ("\(.*\):", ":", content)
        content = re.sub ("\(.*\)", "", content)
        content = re.sub ("\[.*\]", "", content)
    with open (path, 'w' ) as f:
        f.write(content)





