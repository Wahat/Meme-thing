import requests
import json

r = requests.get('https://www.reddit.com/r/dankmemes/top/.json?sort=top&t=day', headers = {'User-agent': 'Chrome'})

theJSON = json.loads(r.text)
links = []
for i in range (1, 20):
    link = theJSON["data"]["children"][i]["data"]["preview"]["images"][0]["source"]["url"]
    print(link)
    links.append(link)

i = "meme"
counter = 0
for link in links: 
    name = i + str(counter) + ".jpeg"
    counter += 1
    print("Downloading meme #" + str(counter))
    response = requests.get(link)
    if response.status_code == 200:
        with open(name, 'wb') as f:
            f.write(response.content)