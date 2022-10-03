import urllib.request, urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
  address = input('Enter location: ')
  if len(address) < 1: break

  params = {}
  params['address'] = address
  params['key'] = 42
  
  url = serviceurl + urllib.parse.urlencode(params)
  uh = urllib.request.urlopen(url)
  data = uh.read()

  try:
    json_data = json.loads(data)
  except:
    json_data = None

  if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
      print('==== Failure To Retrieve ====')
      print(data)
      continue
  place_id = json_data['results'][0]['place_id']
  print(place_id)