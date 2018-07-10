from bs4 import BeautifulSoup
import urllib.request as ulib
import os
import json
import ssl
import sys

def get_soup(url,header):
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    return BeautifulSoup(ulib.urlopen(ulib.Request(url,headers=header), context = gcontext),"html.parser")

def download_images(query, no_of_images=100):
    gquery='+'.join(query.split())
    url="https://www.google.co.in/search?q="+gquery+"&source=lnms&tbm=isch"
    print(url)

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)

    ActualImages=[]# contains the link for Large original images, type of  image
    for ctr, a in enumerate(soup.find_all("div",{"class":"rg_meta"})):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
        print(link, ctr)

    if not os.path.isdir(query):
        os.mkdir(query)
    os.chdir(query)

    downloads = []
    for i , (img_url , Type) in enumerate( ActualImages):
        try:
            img = ulib.urlopen(img_url, context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)).read()
        except Exception as e:
            print("could not load : ", i)
            print(e)
            continue

        if Type=='':
            Type='jpg'
        f = open('%s.%s' %(i, Type), 'wb')
        img = ulib.urlopen(img_url, context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)).read()
        f.write(img)
        f.close()
        downloads.append(i)
        print('downloaded image #', i)
    print('#Images downloaded = ', len(downloads))


if __name__=='__main__':
    for search_term in sys.argv[1:]:
        print(search_term)
        download_images(search_term)


