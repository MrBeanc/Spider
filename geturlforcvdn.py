from bs4 import BeautifulSoup
import re
import urllib2,cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
url='http://ics.cnvd.org.cn/?max=20&offset={i}'
allurl = []
i=0
while(i<300):
    allurl.append(url.format(i=i))
    i=i+20
f=open(r'url.txt','a')
for url in allurl:
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        links = soup.find_all('a', href=re.compile(r"/flaw/"))
        for link in links:
                new_url = link['href']
                f.write('\n')
                f.writelines(new_url)
f.close()


#response = urllib2.urlopen(url)
#soup = BeautifulSoup(response, "html.parser")
#links = soup.find_all('a', href=re.compile(r"/flaw/"))
#for link in links:
#    new_url = link['href']
 #   print new_url
