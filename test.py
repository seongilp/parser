from readability.readability import Document
from urllib.request import Request,urlopen
from urllib.parse import urljoin
import urllib


url = "http://www.ilbe.com/7230766041"

html = urlopen(url).read()

readable_article = Document(html).summary()
readable_title = Document(html).short_title()

print(readable_article)
print(readable_title)

