import requests
from bs4 import BeautifulSoup
from soupsieve import select

episodes = {}

for i in range(1,3):
  
    page = open("data/transcripts/page-" + str(i) + ".html", 'r')
    soup = BeautifulSoup(page.read(), features="lxml")
    #print(soup.prettify())
    #print (soup.select(".topic-titles.row2 h3 a"))
    doc = soup.select(".topic-titles.row2 h3 a")
    for row in doc:
        if row != doc[0] and row != doc[1]: 
            parts = row.text.split(" - ")
            episodes[parts[0]] = {"title": parts[1], "link": row.get("href")}

for key, value in episodes.items():
    parts = key.split("x")
    season = int(parts[0])
    episode = int(parts[1])
    filename = "data/transcripts/S%d-Ep%d" %(season, episode)
    with open(filename, 'wb') as handle:
        headers = {'User-Agent': 'Chrome/78.0.3904.106'}
        response = requests.get(value["link"],headers = headers)
        if response.ok:
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
