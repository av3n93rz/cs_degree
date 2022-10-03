from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://py4e-data.dr-chuck.net/comments_1639984.html').read()
soup = BeautifulSoup(html, 'html.parser')

calculated_sum = sum([int(tag.decode_contents()) for tag in soup('span')])

print(calculated_sum)
