
import requests
import re
import sys
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )


urlmain = 'http://www.cnvd.org.cn'
chromedriver = 'F:\OVFTool\pycharm\untitled\cnvd\chromedriver.exe'
chome_options = webdriver.ChromeOptions()
chome_options.add_argument("--headless")
# chome_options.add_argument(('--proxy-server=' + 'localhost:8080'))
driver = webdriver.Chrome(chromedriver,chrome_options=chome_options)
driver.set_page_load_timeout(5)
driver.set_script_timeout(5)


driver.get(urlmain)

cookies = driver.get_cookies()
print cookies
cookies_save=''
for i in cookies:
    cookies_save += i['name']+'='+i['value']+'; '
cookies_save = str(cookies_save[:-2])
#download = open('down.txt','w')
def refCookie(page_code):
    global headers
    global driver
    global urlMain
    global cookies_save
    if len(page_code) < 100:
        driver.delete_all_cookies()
        driver.get(urlMain)
        cookies = driver.get_cookies()
        cookies_save = ''
        for i in cookies:
            cookies_save += i['name']+'='+i['value']+'; '


def getlast(soup111):
    soup1 = soup111.find_next_sibling('tr')
   # if soup1 is None:
     #   c=1
    try:
      soup = soup1.find('td')
      f1 = soup.text
      f1 = f1.replace('\n', '')
      f1 = f1.strip()
      #download.write( f1+'\n')
      print f1+'\n'
    except:
       # download.write(' ')
       print ' '

def getpack(soup111):
    soup1 = soup111.find_next_sibling('tr')
    soup = soup1.find('td')
    f1 = soup.text
    f1 = f1.replace('\n','')
    f1 = f1.strip()
    soup = soup.find_next_sibling('td')
    try:
        a=soup.text
        a=a.strip()
        #download.write( f1+':'+a+'\n')
        print f1+':'+a+'\n'
    except:
        #download.write(' ')
         print ' '
    return soup1


def getsomething(newurl):
    url = newurl
    headers = {
       'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate, sdch',
       'Accept-Language': 'zh-CN,zh;q=0.8',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/61.0.3163.100 Safari/537.36' ,
       'Cookie': cookies_save
     }
    rs = requests.get(url, headers=headers)
    refCookie(rs.content)
    soupall = BeautifulSoup(rs.content,"html.parser",from_encoding='utf-8')
    soup = soupall.find('div',class_='blkContainerSblk')
    soup = soup.find('h1')
    #download.write( 'title:'+soup.text+'\n')
    print 'title:'+soup.text+'\n'
    #soup = soupall.find('td',class_='alignRight')
    soup1 = soupall.find('tr')
    soup = soup1.find('td')
    f1 = soup.text
    f1 = f1.replace('\n','')
    soup = soup.find_next_sibling('td')
    try:
        a=soup.text
        a=a.strip()
        #download.write( f1+':'+a+'\n')
        print f1+':'+a+'\n'
        soup1 = soupall.find('tr')
    except:
        #download.write(' ')
        print ' '
    i = 1
    while (i < 15):
        soup1 = getpack(soup1)
        i = i + 1
    getlast(soup1)
f = open("url.txt",'r')
for line in f.readlines():
      line = line.replace('\n','')
      line = line.replace('\t', '')
      line = line.strip()
      getsomething(line)
#download.close()
f.close()
driver.quit()
#getsomething('http://www.cnvd.org.cn/flaw/show/CNVD-2017-27958')
#getsomething('http://www.cnvd.org.cn/flaw/show/CNVD-2017-27960')
#getsomething('http://www.cnvd.org.cn/flaw/show/CNVD-2017-26427')
#getsomething('http://www.cnvd.org.cn/flaw/show/CNVD-2017-25720')
#getsomething('http://www.cnvd.org.cn/flaw/show/CNVD-2017-25723')
#download.close()
