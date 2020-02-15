import requests
import re
import csv
from bs4 import BeautifulSoup

url = requests.get("https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains")

soup = BeautifulSoup(url.content, 'html.parser')

with open('TLD.csv','w',newline='') as csvfile:
    File = csv.writer(csvfile, delimiter=' ', quotechar='|')
    for link in soup.findAll('a', text=re.compile(r'^\.')):
        a = link.text
        print("Top-level domain is", a)
        if link.text != ' ' and link.text.count('.') == 1:
            try:
                r = requests.get("http://example"+a)
                if r.status_code == 200:
                    print(f"Second level domain is valid, http://example{link.text} returns {r.status_code}")
                    File.writerow([f"Second level domain is valid, http://example{link.text} returns {r.status_code}"])
                else:
                    print(f"Second level domain is invalid, http://example{link.text} returns {r.status_code}")
                    File.writerow([f"Second level domain is invalid, http://example{link.text} returns {r.status_code}"])
            except requests.ConnectionError:
                print(a, "Invalid Response due to connection error")
                File.writerow(["Invalid Response due to connection error"])
