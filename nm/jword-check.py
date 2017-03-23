import requests
from bs4 import BeautifulSoup

def check():
    uri = raw_input("Enter the URI that you wish to check: ")
    word = raw_input("Enter the word you wish to check for: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(uri, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    if str(soup).find(word) >= 1:
        print("Found It!")
    else:
        print("I couldn't find it")

check()
