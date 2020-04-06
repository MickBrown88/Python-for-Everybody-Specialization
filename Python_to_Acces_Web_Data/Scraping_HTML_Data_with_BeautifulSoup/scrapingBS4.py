
from urllib import request
from bs4 import BeautifulSoup as bs
html=request.urlopen('http://python-data.dr-chuck.net/comments_389063.html').read()
soup = bs(html)
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)