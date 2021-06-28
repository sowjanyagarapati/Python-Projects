#requests module to get the html elements from the url
import requests
import os

req_url = requests.get("https://www.example.com")
req_url = req_url.text

#beautifulsoup for parsing and reading the html content
from bs4 import BeautifulSoup
soup = BeautifulSoup(req_url)

print(soup)

#saving the html content into a file
file = open("webscrapping.html","w+",encoding='utf-8')
file.write(str(soup))
file.close()
print("saved")
