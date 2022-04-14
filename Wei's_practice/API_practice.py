import requests
import json
my_headers = {'Authorization': 'Client-ID 66c1e33f571d4d4'}
res = requests.get('https://api.imgur.com/3/album/iiJQ1TF/images', headers=my_headers)
x = json.loads(res.text)['data']
for i in x:
    print(i['title'])
    print(i['link'])





