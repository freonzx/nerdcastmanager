import urllib.request

def download(filename,url):
	download = urllib.request.urlretrieve(url,filename)
	

download("nerdcast566.mp3","https://nerdcast-cdn.jovemnerd.com.br/nerdcast_566_memoria.mp3")
