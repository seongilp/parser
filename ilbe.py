from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from readability.readability import Document
import urllib

base_url = "http://ilbe.com/ilbe"

url_request = Request(base_url,headers={'User-Agent': 'Mozilla/5.0'})
ilbe = urlopen(url_request).read()

bs4_ilbe = BeautifulSoup(ilbe,"html.parser")

#find_mytr = bs4_ilbe.find_all("td",attrs={'class':"bg1"})
find_mytr = bs4_ilbe.find_all("tr",{"bg1","bg2"})

for t in find_mytr:
    title_and_link = t.findAll("a")[0]
    link = title_and_link["href"]
    full_url = urljoin(base_url,link)
    article = urlopen(full_url).read()
    r_article = Document(article).summary()
    r_title = Document(article).short_title()
    bs_article = BeautifulSoup(article,"html.parser")
    print("URL: "+full_url)
    #print("Title: "+t.find('td',attrs={'class':'t_subject'}).get_text(strip=True).encode('cp949','ignore').decode('cp949'))
    print("Title: "+r_title)
#    print("Text: "+r_article)

