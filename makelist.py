import requests
from bs4 import BeautifulSoup
base_url = 'https://jovemnerd.com.br/feed-nerdcast/'

r = requests.get(base_url)

soup = BeautifulSoup(r.text, "html.parser")

for link in soup.find_all(['link', 'title','enclosure url=']):
	print(link)
	