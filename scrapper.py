import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

page_url = 'https://krcl.org/playlist/?page=1'
#class = playlistitem-name

response = http.request('GET', page_url)

soup = BeautifulSoup(response.data, 'html.parser')

item_divs = soup.findAll("div", {"class": "playlistitem-name"})

for item in item_divs:
  print(item)
