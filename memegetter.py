#Author: Kevin Shen
import requests
import json
from selenium import webdriver
import time
USER = ""
PASS = ""
CHAT = ''
r = requests.get('https://www.reddit.com/r/dankmemes/top/.json?sort=top&t=day', headers = {'User-agent': 'Chrome'})
theJSON = json.loads(r.text)
links = []
for i in range (1, 20):
    link = theJSON["data"]["children"][i]["data"]["preview"]["images"][0]["source"]["url"]
    #print(link)
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
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# Open new Selenium WebDriver for Chrome
browser=webdriver.Chrome(chrome_options=chrome_options)
# Open chat
browser.get(CHAT)
browser.find_element_by_id("email").send_keys(USER)
browser.find_element_by_id("pass").send_keys(PASS)
login = browser.find_element_by_id("loginbutton").click()
imageinp = browser.find_element_by_class_name("_260t").send_keys("/path/to/meme")
buttons = browser.find_element_by_class_name("_5rpb")
sender = browser.find_element_by_class_name("notranslate")
print(type(sender))
sender.send_keys(u'\ue007')
start = time.time()
end = time.time()
while ((end-start) < 5):
    end = time.time()
browser.close()
