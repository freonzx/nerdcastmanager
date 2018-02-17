import os
import sys

with open(os.path.join(sys.path[0],'download_list.txt')) as f:
    lines = f.read().splitlines()
    lines = list(reversed(lines))
	
def name(url):
	return url.split('/')[3]