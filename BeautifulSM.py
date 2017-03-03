from bs4 import BeautifulSoup

import requests

import time

import difflib

url = raw_input("Enter website to monitor: ")

t = int(raw_input("Wait time: "))

while True:
	r1  = requests.get(url)
	data1 = r1.text
	soup1 = BeautifulSoup(data1)

	time.sleep(t)

	r2  = requests.get(url)
	data2 = r2.text
	soup2 = BeautifulSoup(data1)

	if soup1 == soup2:
		print("No change")
	else:
		print("Change!")
		d = difflib.Differ()
		diff = d.compare(soup1, soup2)
		print '\n'.join(diff)
