from bs4 import BeautifulSoup
import urllib.request as ulib
import ssl

def get_soup(url,header):
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    return BeautifulSoup(ulib.urlopen(ulib.Request(url,headers=header), context = gcontext),"html.parser")

url = 'https://en.wikipedia.org/wiki/List_of_Indian_film_actors'
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)

f=open('filmstars.txt', 'w')
for ctr, a in enumerate(soup.find_all("div",{"class":"div-col columns column-width"})):
	x=a.findAll('ul')[0].findAll('li')
	for y in x:
		name = str(y.string)
		f.write(name+'\n')
		print(name)
f.close()
