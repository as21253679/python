#https://www.sslproxies.org/
from urllib import request
import sys
from bs4 import BeautifulSoup

url = "https://dir.twseo.org/ip-check.php"
proxy_support = request.ProxyHandler({'https':'202.61.84.238:3128'})
opener = request.build_opener(proxy_support)
opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
request.install_opener(opener)
response = request.urlopen(url)

data = response.read()

#使用BeautifulSoup解析原始碼
sp=BeautifulSoup(data,'lxml')
m=sp.select('.showbig')[0]
ip=m.find_all('font')[0].text
print("IP:"+ip)


fp = open("text.txt", "a", encoding="utf-8")
#fp.write(sp.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
fp.close()