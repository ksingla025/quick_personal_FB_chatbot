#!/usr/bin/python


import glob
from bs4 import BeautifulSoup

DATA = "./fb_data/messages/*.html"

out_file = "./seq2seq-chatbot/data/fb_chat/"

files = glob.glob(DATA)

total = 0
mine = 0
others = 0
for file in files:
	
	html_text = open(file,'r')
	soup = BeautifulSoup(html_text, 'lxml')
	
	dialogues = soup.find_all('p')
	name_date = soup.find_all('span')

	k = 0
	try:
		for i in range(0,len(dialogues)):

			dialogue = dialogues[i].text
			k = k + 2
			if len(name_date[k].text.split()) <  4:
				name = name_date[k].text
			else:
				k = k - 1
				name = name_date[k].text

			if name == "Karan Singla":
				mine = mine + 1
			else:
				others = others + 1

			if dialogue.strip() != '':
				print(dialogue)
	except:
		continue
#	total = total + len(soup.find_all('p'))

print("#total messages", total)
print("#my_messages", mine)
print("#others messages", others)
