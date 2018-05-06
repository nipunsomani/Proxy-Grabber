from bs4 import BeautifulSoup
import requests
import base64

ip_port_combined=[]
ip=[]
port=[]

proxy_type=[]

pages=int(input("How many pages you want to access? 1 page contains 14 proxies :"))


for i in range(1,pages+1):

	print("[+] Grabbing Proxies from page %d"%i)
	
	url="https://proxy-list.org/english/index.php?p=%d"%i
	headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
	client=requests.get(url, headers=headers)
	html=client.text

	data=BeautifulSoup(html,'html.parser')
	getdata=data.findAll("li", class_="proxy")
	for i in getdata:
		ip_port=base64.b64decode(i.getText()[7:-2])
		if ip_port == "":
			pass
		else:
			ip_port_combined.append(ip_port)

	for i in ip_port_combined:
		getip,getport=i.split(":")
		ip.append(getip)
		port.append(getport)

	ptype=data.findAll("li", class_="https")
	for i in ptype:
		proxy_type.append(str(i.getText()))

	f=open("proxies.txt","a+")
	for a,b,c in zip(proxy_type,ip,port):
		f.write("%s %s %s \n" % (a,b,c))
	f.close()

print("Successfully Completed! Please find all the proxies in proxies.txt")
