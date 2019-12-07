#scraping code modified from Mark Needham's Python NLTK/Neo4j: Analysing the transcripts of How I Met Your Mother
import requests
from bs4 import BeautifulSoup
from soupsieve import select

episodes = {}

for i in range(3,9):
  
    page = open("data/html/page-" + str(i) + ".html", 'r')
    soup = BeautifulSoup(page.read(), features="lxml")
    doc = soup.select(".topic-titles.row2 h3 a")
    for row in doc:
        if row != doc[0] and row != doc[1]: 
            parts = row.text.split(" - ")
            episodes[parts[0]] = {"title": parts[1], "link": row.get("href")}

website = "http://transcripts.foreverdreaming.org"
for key, value in episodes.items():

    parts = key.split("x")
    season = int(parts[0])
    episode = int(parts[1])

    filename = "data/transcripts/S%d-Ep%d.txt" %(season, episode)
    link = value["link"] #for pages 3-14
    link = website+ link[1:] #for pages 3-14
  
    with open(filename, 'wb') as handle:
        headers = {'User-Agent': 'Chrome/78.0.3904.106'}
        response = requests.get(link,headers = headers) #use value["link"] instead of link for pages 1 and 2 #use link for other pages
        if response.ok:
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
