from bs4 import BeautifulSoup
import requests
import time
import difflib

url = raw_input("Enter website to monitor: ")
# set the site headers to be used by the requests library, this tells requests to use the same user agent every time it refreshes
# just in case requests changes user agents for some reason, not sure but this will/should prevent that
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
t = int(raw_input("Wait time: "))

while True:
	r1  = requests.get(url, headers=headers)
	data1 = r1.text
	soup1 = BeautifulSoup(data1, "html.parser")

	time.sleep(t)

	r2  = requests.get(url)
	data2 = r2.text
	soup2 = BeautifulSoup(data2, "html.parser")

	if soup1 == soup2:
		print("No change")
	else:
		l1 = str(soup1).split(' ')
		l2 = str(soup2).split(' ')
		d = difflib.Differ();
		dif = list(d.compare(l1, l2));
		print(" ".join(['<b>'+i[2:]+'</b>' if i[:1] == '+' else i[2:] for i in dif if not i[:1] in '-?']))
