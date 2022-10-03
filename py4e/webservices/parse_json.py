

from urllib.request import urlopen
import json

url = 'https://py4e-data.dr-chuck.net/comments_1639987.json'

fhand = urlopen(url).read()
data = json.loads(fhand)

print(sum([comment['count'] for comment in data['comments']]))
