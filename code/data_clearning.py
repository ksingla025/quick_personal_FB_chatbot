#!/usr/bin/python


import glob
from bs4 import BeautifulSoup

from seq2seq-chatbot.data.twitter import data

DATA = "./data/messages/*.html"

out_files = "./seq2seq-chatbot/data/fb_chat/"
out_text_file = open(out_files+"fb_chat.txt",'w')


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
				out_text_file.write(dialogue+"\n")
	except:
		continue
#	total = total + len(soup.find_all('p'))
out_text_file.close()

data.FILENAME = out_text_file+"fb_chat.txt"
data.process_data()

print("#total messages", total)
print("#my_messages", mine)
print("#others messages", others)
