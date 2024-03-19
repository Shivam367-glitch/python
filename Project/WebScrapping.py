#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "http://www.values.com/inspirational-quotes" 
r = requests.get(URL) 

#html parsing
soup = BeautifulSoup(r.content, 'html5lib') 

quotes=[] # a list to store quotes 


# getting all div in page having id ---'all_quotes'
table = soup.find('div', attrs = {'id':'all_quotes'}) 


# here table is contains of multiple div with class as col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top
for row in table.findAll('div', 
						attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}): 
	quote = {} 
	quote['theme'] = row.h5.text 
	quote['url'] = 'https://www.passiton.com'+row.a['href'] 
	quote['img'] = row.img['src'] 
	quote['lines'] = row.img['alt'].split(" #")[0] 
	quote['author'] = row.img['alt'].split(" #")[1] 
	quotes.append(quote) 

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
