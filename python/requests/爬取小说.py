import requests
from lxml import etree
url = 'https://m.ddxs.cc/ddxs/167980/14073263.html'

r = requests.get(url)
print(r.text)
html = etree.HTML(r.text)
c = html.xpath()