import os
import sys
import urllib.request
global url # global variable to be used in dlProgress
from pathlib import Path

from nerdcast_parser import update

def download(url):
	#download = urllib.request.urlretrieve(url,filename) deprecated
	urllib.request.urlretrieve(url, url.split('/')[3] , reporthook=dlProgress)
	
with open(os.path.join(sys.path[0],'download_list.txt')) as f:
    lines = f.read().splitlines()

lines = list(reversed(lines))
	
def dlProgress(count, blockSize, totalSize):
	percent = int(count*blockSize*100/totalSize)
	sys.stdout.write("\r" + "...%d%%" % percent)
	sys.stdout.flush()
	
def banner():
	print(' _   _              _ __  __                                   ')
	print('| \ | | ___ _ __ __| |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ')
	print('|  \| |/ _ \ \'__/ _` | |\/| |/ _` | \'_ \ / _` |/ _` |/ _ \ \'__|')
	print('| |\  |  __/ | | (_| | |  | | (_| | | | | (_| | (_| |  __/ |   ')
	print('|_| \_|\___|_|  \__,_|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   ')
	print('					       |___/           ')
	print('#################################################################')

def down_all():

	for cast in lines:
		url = cast
		
		arquivo = Path(os.path.join(sys.path[0]+'\\Nerdcasts\\'+url.split('/')[3]))
		
		if arquivo.is_file(): #Check if archive already exists then skips it
			pass
		else:
			print('\n\n[*] Baixando %s' % url.split('/')[3])
			download(cast)
		
def menu():
	os.chdir(os.path.join(sys.path[0]+'\\Nerdcasts\\'))
	os.system('cls')
	banner()
	print('[1] Baixar Todos Nerdcasts')
	print('[2] Baixar Nerdcast especifico')
	print('[3] Baixar Range (Ex: 102-238)')
	print('[4] Atualizar Database de Nerdcasts')
	print('[5] Ver lista de Nerdcasts')
	print('[6] Sair')
	op = int(input())
	
	if op == 1:
		down_all()
	elif op == 2:
		specific = int(input('[*] Nerdcast Numero:'))
		if specific is not None:
			url = lines[specific-1]
			print('\n\n[*] Baixando %s' % lines[specific-1].split('/')[3])
			download(url)
			#os.system('cls')
			menu()
	elif op == 3:
		inicio = int(input('[*] Digite por onde começar: '))
		termino = int(input('[*] Digite e onde terminar: '))
		if inicio < termino:
			for x in range (inicio,termino):
				url = lines[x]
				print('\n\n[*] Baixando %s' % lines[x].split('/')[3])
				download(lines[x-1])
		else:
			pass
	elif op == 4:
		os.chdir(os.path.join(sys.path[0]))
		print('[*] Atualizando database de links.')
		update()
		menu()
	elif op == 5:
		print('[*] Lista:')
		for idx, val in enumerate(lines):
			print(idx+1, val.split('/')[3])
		input('[*] Digite qualquer para voltar ao menu.')
		menu()
		
	elif op == 6:
		exit
		

menu()





