import requests
from bs4 import BeautifulSoup

url=raw_input("Enter the Wiki URL to test: ")
baseurl="https://en.wikipedia.org"


r=requests.get(url)
data=r.text
soup=BeautifulSoup(data)

print soup.title.text

count=0

flag=1

while(flag):
	newurl=''
	x=0
	b=soup.find_all('p')
	while(x in range(len(b))):
		if b[x].text == '':
			x+=1
		else:
			m=b[x].find_all('a')
			print "Khoj liya"
			break
	
	c=True
	i=0
	while c:
		if ("#cite" in m[i]['href']) or ("Help:" in m[i]['href']) or ("File:" in m[i]['href']) or ("upload.wikimedia" in m[i]['href']):
			print i 
			i+=1
		else:
			c=False
			khoj=m[i]['href']
			

	newurl=baseurl+khoj
	print newurl
	r=requests.get(newurl)
	data=r.text
	soup=BeautifulSoup(data)
	print soup.title.text
	count+=1
	print count
	if "Philosophy" in soup.title.text:
		flag = 0	
	else:
		print "No Philosophy"

print count
