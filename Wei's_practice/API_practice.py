import requests
import json
my_headers = {'Authorization': 'Client-ID 66c1e33f571d4d4'}
res = requests.get('https://api.imgur.com/3/album/aOXKX4b/images', headers=my_headers)
content = json.loads(res.text)['data']

for i in content:
    print('ID: ', i['id'])
    print('Title: ', i['title'])
    print('Description: ', i['description'])
    print('Link: ', i['link'])







