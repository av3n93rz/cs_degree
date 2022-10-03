from urllib.request import urlopen
from bs4 import BeautifulSoup

last_name = None

url = 'http://py4e-data.dr-chuck.net/known_by_Aleksandr.html'

i = 0

while i < 7:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup('a')[17]
    url = tag['href']
    last_name = tag.decode_contents()
    i = i + 1

print(last_name)