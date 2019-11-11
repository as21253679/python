#https://www.sslproxies.org/  			#https
#http://www.freeproxylists.net/zh/		#http
from urllib import request
import sys
from bs4 import BeautifulSoup
import threading
import time

t=[]
ip_array = ['221.126.249.100:8080',
			'119.235.248.165:8080',
			'149.28.145.78:3128',
			'182.73.214.78:8080',
			'119.76.140.77:8080',
			'36.70.213.151:8080',
			'46.209.119.58:59292',
			]
def request_process(number,proxy_ip):
	url = "https://cmp.nkuht.edu.tw/info/ip.asp"	#查詢IP
	#url = "https://ithelp.ithome.com.tw/questions/10194109"		#IT home
	for i in range(0,1000):
		proxy_support = request.ProxyHandler({'https':proxy_ip})
		opener = request.build_opener(proxy_support)
		opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
		request.install_opener(opener)
		try:
			response = request.urlopen(url)
			print("number:",number," 次數:",i)
			
			#使用BeautifulSoup解析原始碼
			#data = response.read()
			#sp=BeautifulSoup(data,'lxml')
			#m=sp.select('b')[0]
			#ip=m.find_all('font')[0].text
			#print(ip)
		except:
			print("錯誤IP:",proxy_ip)
			return

for i in range(0,len(ip_array)):
	# 建立一個子執行緒
	t.append(threading.Thread(target = request_process, args = (i,ip_array[i],)))
	# 執行該子執行緒
	t[i].start()
	# 等待 t 這個子執行緒結束
	#t[i].join()
	