import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

page_url = 'https://krcl.org/playlist/?page=1'
#class = playlistitem-name

response = http.request('GET', page_url)

soup = BeautifulSoup(response.data, 'html.parser')

item_divs = soup.findAll("div", {"class": "playlistitem-name"})

for item in item_divs:
  alltext = item.findAll('h3')
  first_line = alltext[0]
  album = alltext[1].text

  artist = first_line.findAll('b')
  artist = artist[0].text

  allstr = alltext[0].text.strip()
  line_index = allstr.find('|')
  song = allstr[line_index+2:]
  
  print("artist:", artist, "song:", song, "album:", album)
