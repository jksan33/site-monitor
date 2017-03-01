from bs4 import BeautifulSoup

import requests

import time

url = raw_input("Enter a website to extract the URL's from: ")

t = int(raw_input("Wait time: "))

while True:
	r1  = requests.get("http://" +url)
	data1 = r1.text
	soup1 = BeautifulSoup(data1)

	time.sleep(t)

	r2  = requests.get("http://" +url)
	data2 = r2.text
	soup2 = BeautifulSoup(data1)

	if soup1 == soup2:
		print("No change")
	else:
		print("Change!")
