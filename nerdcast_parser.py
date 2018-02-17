import feedparser
from bs4 import BeautifulSoup

def update():
	nerdcastrss = 'https://jovemnerd.com.br/feed-nerdcast/'

	feed = feedparser.parse(nerdcastrss)

	fh = open('download_list.txt', 'a')

	items = feed['items']

	'''for post in feed.entries:
		print (post.links + "\n")'''
		
	for numero in range(0,750):
		try:
			fh.write(items[numero]['links'][1]['href']+"\n")
		except:
			pass
		