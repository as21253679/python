#https://www.sslproxies.org/  			#https
#http://www.freeproxylists.net/zh/		#http
from urllib import request
import sys
from bs4 import BeautifulSoup
import threading
import time
import requests

count=0
error=0
t=[]
ip_array=[]
def get_all_proxy_ip():
	#獲取網頁資料
	url='https://www.sslproxies.org/'
	#使用get方式向網頁發送請求
	html=requests.get(url)
	#使用utf-8方式編碼讀取網頁
	html.encoding='utf-8'
	#自訂網頁表頭，讓電腦模擬瀏覽器操作網頁，騙過網頁伺服器
	headers={'user-agent':'Mozilla/5.0'}
	#使用BeautifulSoup解析原始碼
	sp=BeautifulSoup(html.text,'lxml')
	for m in sp.select('tbody')[0].select('tr'):
		ip=m.find_all('td')[0].text
		port=m.find_all('td')[1].text
		ip_array.append("%s:%s"%(ip, port))

def request_process(url,max_times,time_out,number,proxy_ip):
	global count,error
	proxy_error_count=0
	for i in range(0,1000):
		proxy_support = request.ProxyHandler({'https':proxy_ip})
		opener = request.build_opener(proxy_support)
		opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
		request.install_opener(opener)
		try:
			response = request.urlopen(url,timeout=int(time_out)) #是否需要response
			#使用BeautifulSoup解析原始碼
			#data = response.read()
			#sp=BeautifulSoup(data,'lxml')
			#m=sp.select('b')[0]
			#ip=m.find_all('font')[0].text
			#print("編號:",number," IP:",ip)

			if count>int(max_times):
				return
			count += 1
			print("成功次數:",count,"  錯誤:",error)
			#print("編號:",number," proxy成功次數:",i)
		except Exception as e:
			proxy_error_count += 1
			if proxy_error_count >= 3:
				error += 1
				#print("編號:",number,"錯誤IP:",proxy_ip)
				return

def main():
	if len(sys.argv)<4:
		print("後面要加這3個參數:")
		print("要連入的網址 最大執行次數(500) timeout(10)")
		return
	get_all_proxy_ip()
	print("已獲得proxy ip")
	for i in range(0,len(ip_array)):
		# 建立一個子執行緒
		t.append(threading.Thread(target = request_process, args = (sys.argv[1],sys.argv[2],sys.argv[3],i,ip_array[i],)))
		# 執行該子執行緒
		t[i].start()
		# 等待 t 這個子執行緒結束
		#t[i].join()
	
if __name__ == "__main__":
    main()